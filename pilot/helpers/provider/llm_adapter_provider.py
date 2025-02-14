import os
from typing import Dict, Callable

from helpers.adapters.llm_adapter import LlmAdapter
from helpers.provider.anthropic_adapter_provider import AnthropicAdapterProvider
from helpers.provider.chat_gpt_adapter_provider import ChatGptAdapterProvider
from helpers.provider.terminal_adapter_provider import TerminalAdapterProvider
from logger.logger import logger


LLM_PLATFORM_MAPPER: Dict[str, Callable] = {
        "OPENAI": ChatGptAdapterProvider.get_chat_gpt_adapter,
        "TERMINAL": TerminalAdapterProvider.get_adapter,
        "ANTHROPIC": AnthropicAdapterProvider.get_anthropic_adapter
    }


class LlmAdapterProvider:

    @staticmethod
    def get_llm_adapter(llm_platform: str = None) -> LlmAdapter:
        logger.info(f"Instantiating LlmProvider to platform: {llm_platform}")
        provider_function = LLM_PLATFORM_MAPPER.get(llm_platform)
        return provider_function()
