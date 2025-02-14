import platform
from typing import Dict

from helpers.agents.agent import Agent
from helpers.agents.conversational_agent import ConversationalAgent
from helpers.provider.conversation_agent_provider import ConversationAgentProvider
from logger.logger import logger
from utils.style import color_green_bold
from const.roles import Roles


class Architect(Agent):

    def __init__(self):
        super().__init__(Roles.ARCHITECT.value)
        self.conversational_agent: ConversationalAgent = (ConversationAgentProvider.
                                                     get_conversational_agent(self.role, self.role_description))

    def get_architecture(self, project_description: str, specs: str) -> str:

        print(color_green_bold("Planning project architecture...\n"))
        logger.info("Planning project architecture...")

        self.conversational_agent.append_prompt_to_messages('architecture/technologies_v2.prompt',
                                                       {'project_description': project_description,
                                                        'project_specs': specs})

        # conversational_agent.append_prompt_to_messages("schemas/architecture_json_schema.prompt")

        llm_response = self.conversational_agent.send_messages()

        architecture = llm_response["content"]
        self.conversational_agent.append_message({"role": self.conversational_agent.llm_role, "content": architecture})

        logger.info(f"Final architecture: {architecture}")

        return architecture

    def get_end_2_end_use_cases(self) -> str:

        print(color_green_bold("Planning project end to end use cases...\n"))
        logger.info("Planning project end to end use cases...")

        self.conversational_agent.append_prompt_to_messages("architecture/end2end.prompt")

        llm_response = self.conversational_agent.send_messages()
        end_2_end_use_cases = llm_response["content"]

        logger.info(f"Final end to end use cases: {end_2_end_use_cases}")
        return end_2_end_use_cases

    def get_use_cases_diagram(self) -> str:
        print(color_green_bold("Generating use cases mermaid diagrams...\n"))
        logger.info("Generating use cases mermaid diagrams...")

        self.conversational_agent.append_prompt_to_messages("architecture/use_cases.prompt")

        llm_response = self.conversational_agent.send_messages()
        use_cases_mermaid_diagram = llm_response["content"]

        logger.info(f"Use case diagrams: {use_cases_mermaid_diagram}")
        return use_cases_mermaid_diagram

    def get_architecture_diagram(self) -> str:
        print(color_green_bold("Generating architecture mermaid diagram...\n"))
        logger.info("Generating architecture mermaid diagram...")

        self.conversational_agent.append_prompt_to_messages("architecture/architecture_diagram.prompt")

        llm_response = self.conversational_agent.send_messages()
        architecture_mermaid_diagram = llm_response["content"]

        logger.info(f"Architecture diagram: {architecture_mermaid_diagram}")
        return architecture_mermaid_diagram
