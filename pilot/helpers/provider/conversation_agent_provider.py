import os
from typing import Dict

from helpers.agents.conversational_agent import ConversationalAgent
from helpers.provider.llm_adapter_provider import LlmAdapterProvider
from const.roles import Roles
from logger.logger import logger

default_llm_platform: str = os.environ["DEFAULT_LLM_PLATFORM"]

role_to_llm_platform_mapper: Dict[str, str] = {
    Roles.ARCHITECT.value: os.environ.get("ARCHITECT_LLM_PLATFORM", default_llm_platform),
    Roles.PRODUCT_OWNER.value: os.environ.get("PRODUCT_OWNER_LLM_PLATFORM", default_llm_platform),
    Roles.SPEC_WRITER.value: os.environ.get("SPEC_WRITER_LLM_PLATFORM", default_llm_platform),
    Roles.TECH_LEAD.value: os.environ.get("TECH_LEAD_LLM_PLATFORM", default_llm_platform)
}


class ConversationAgentProvider:

    @staticmethod
    def get_conversational_agent(agent_role: str, role_description: str) -> ConversationalAgent:
        logger.info(f"Getting conversational agent to {agent_role}")
        platform = role_to_llm_platform_mapper.get(agent_role, default_llm_platform)
        llm_adapter = LlmAdapterProvider.get_llm_adapter(platform)
        return ConversationalAgent(agent_role, role_description, llm_adapter)
