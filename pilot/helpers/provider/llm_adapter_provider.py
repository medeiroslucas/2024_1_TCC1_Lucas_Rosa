import os
from typing import Dict, Callable

from helpers.adapters.llm_adapter import LlmAdapter
from helpers.provider.chat_gpt_adapter_provider import ChatGptAdapterProvider
from logger.logger import logger


LLM_PLATFORM_MAPPER: Dict[str, Callable] = {
        "OPENAI": ChatGptAdapterProvider.get_chat_gpt_adapter
    }


class LlmAdapterProvider:

    @staticmethod
    def get_llm_adapter(platform: str = None) -> LlmAdapter:
        llm_platform = platform if platform else os.environ["LLM_PLATFORM"]

        logger.info(f"Instantiating LlmProvider to platform: {llm_platform}")
        provider_function = LLM_PLATFORM_MAPPER.get(llm_platform)
        return provider_function()
