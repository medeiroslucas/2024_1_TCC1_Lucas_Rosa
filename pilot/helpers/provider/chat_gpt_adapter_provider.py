import os

from helpers.adapters.chat_gpt_adapter import ChatGptAdapter


class ChatGptAdapterProvider:

    @staticmethod
    def get_chat_gpt_adapter() -> ChatGptAdapter:
        endpoint = os.environ["OPEN_AI_ENDPOINT"]
        model = os.environ["OPEN_AI_MODEL_NAME"]
        api_key = os.environ["OPEN_AI_API_KEY"]

        return ChatGptAdapter(endpoint, model, api_key)
