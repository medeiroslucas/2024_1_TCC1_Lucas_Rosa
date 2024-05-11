from helpers.agents.conversational_agent import ConversationalAgent
from helpers.provider.llm_adapter_provider import LlmAdapterProvider


class ConversationAgentProvider:

    @staticmethod
    def get_conversational_agent(agent_role: str, role_description: str) -> ConversationalAgent:
        llm_adapter = LlmAdapterProvider.get_llm_adapter()
        return ConversationalAgent(agent_role, role_description, llm_adapter)
