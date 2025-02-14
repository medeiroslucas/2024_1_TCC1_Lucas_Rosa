from typing import Dict

from helpers.agents.agent import Agent
from helpers.agents.conversational_agent import ConversationalAgent
from helpers.provider.conversation_agent_provider import ConversationAgentProvider
from logger.logger import logger
from utils.style import color_green_bold
from const.roles import Roles


class TechLead(Agent):

    def __init__(self):
        super().__init__(Roles.TECH_LEAD.value)

    def get_development_plan(self, main_description: str, project_specs: str, architecture: str, use_cases: str) -> Dict:
        conversational_agent: ConversationalAgent = (ConversationAgentProvider.
                                                     get_conversational_agent(self.role, self.role_description))

        # DEVELOPMENT PLANNING
        print(color_green_bold("Generating the action plan for development...\n"))
        logger.info("Generating the action plan for development...")

        conversational_agent.append_prompt_to_messages('development/plan.prompt',
                                                       {
                                                           "main_description": main_description,
                                                           "project_specs": project_specs,
                                                           "architecture": architecture,
                                                           "use_cases": use_cases
                                                       })

        llm_response = conversational_agent.send_messages()
        development_plan = llm_response["content"]

        logger.info(f"Final development plain: {development_plan}")
        return development_plan
