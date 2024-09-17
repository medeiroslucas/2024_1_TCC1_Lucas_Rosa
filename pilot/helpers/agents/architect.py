import platform
from typing import Dict

from helpers.agents.agent import Agent
from helpers.agents.conversational_agent import ConversationalAgent
from helpers.provider.conversation_agent_provider import ConversationAgentProvider
from logger.logger import logger
from utils.style import color_green_bold


class Architect(Agent):

    def __init__(self):
        super().__init__('architect')

    def get_architecture(self, project_description: str, specs: str) -> str:

        print(color_green_bold("Planning project architecture...\n"))
        logger.info("Planning project architecture...")

        conversational_agent: ConversationalAgent = (ConversationAgentProvider.
                                                     get_conversational_agent(self.role, self.role_description))

        conversational_agent.append_prompt_to_messages('architecture/technologies_v2.prompt',
                                                       {'project_description': project_description,
                                                        'project_specs': specs})

        # conversational_agent.append_prompt_to_messages("schemas/architecture_json_schema.prompt")

        llm_response = conversational_agent.send_messages()

        architecture = llm_response["content"]

        logger.info(f"Final architecture: {architecture}")

        return architecture
