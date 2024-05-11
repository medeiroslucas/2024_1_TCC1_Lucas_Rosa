from helpers.agents.conversational_agent import ConversationalAgent
from helpers.agents.agent import Agent
from utils.style import color_green_bold, color_yellow_bold, color_white_bold
from prompts.prompts import ask_user
from const.messages import AFFIRMATIVE_ANSWERS
from helpers.provider.conversation_agent_provider import ConversationAgentProvider


INITIAL_PROJECT_HOWTO_URL = "https://github.com/Pythagora-io/gpt-pilot/wiki/How-to-write-a-good-initial-project-description"

SHORT_DESCRIPTION_MESSAGE = (
    "Your project description seems a bit short. "
    "The better you can describe the project, the better GPT Pilot will understand what you'd like to build.\n\n"
    f"Here are some tips on how to better describe the project: {INITIAL_PROJECT_HOWTO_URL}\n\n"
)


class SpecWriter(Agent):
    def __init__(self):
        super().__init__('spec_writer')

    def create_spec(self, initial_description):
        if self.is_initial_description_enough(initial_description):
            return initial_description

        specs = self.generate_project_specs(initial_description)
        missing_info = self.review_spec(initial_description, specs)
        if missing_info:
            specs += "\nAdditional info/examples:\n" + missing_info

        return specs

    def generate_project_specs(self, initial_description):

        print(color_yellow_bold(SHORT_DESCRIPTION_MESSAGE))
        print(color_green_bold("Let's start by refining your project idea:"))

        conversational_agent: ConversationalAgent = (ConversationAgentProvider.
                                                     get_conversational_agent(self.role, self.role_description))

        conversational_agent.append_prompt_to_messages('spec_writer/ask_questions.prompt')
        user_response = initial_description

        while True:
            conversational_agent.append_user_input_to_messages(user_response)
            llm_response: str = conversational_agent.send_messages()["content"]
            if not llm_response:
                continue

            llm_response = llm_response.strip()
            if len(llm_response) > 500:
                print(color_white_bold("\n" + llm_response + "\n\n\n"))
                user_response = ask_user(
                    "Can we proceed with this project description? If so, just press ENTER."
                    " Otherwise, please tell me what's missing or what you'd like to add.",
                    hint="Does this sound good, and does it capture all the information about your project?",
                    require_some_input=False
                )
                if user_response:
                    user_response = user_response.strip()
                if user_response.lower() in AFFIRMATIVE_ANSWERS + ['continue']:
                    break
            else:
                user_response = ask_user(llm_response)
                if user_response and user_response.lower() == 'skip questions':
                    conversational_agent.append_user_input_to_messages('This is enough clarification, you have all the'
                                                                       ' information. Please output the spec now,'
                                                                       ' without additional comments or questions.')
                    llm_response = conversational_agent.send_messages()["content"]
                    break

        return llm_response

    def review_spec(self, initial_prompt, spec):
        conversational_agent: ConversationalAgent = (ConversationAgentProvider.
                                                     get_conversational_agent(self.role, self.role_description))
        conversational_agent.append_prompt_to_messages('spec_writer/review_spec.prompt', {
            "brief": initial_prompt,
            "spec": spec,
        })
        llm_response: str = conversational_agent.send_messages(temperature=0)["content"]
        if not llm_response:
            return None
        return llm_response.strip()

    @staticmethod
    def is_initial_description_enough(initial_description: str) -> bool:
        return len(initial_description) > 1500
