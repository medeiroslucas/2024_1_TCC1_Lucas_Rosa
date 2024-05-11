import os

from helpers.adapters.chat_gpt_adapter import ChatGptAdapter


class ChatGptAdapterProvider:

    @staticmethod
    def get_chat_gpt_adapter() -> ChatGptAdapter:
        endpoint = os.environ["ENDPOINT"]
        model = os.environ["MODEL_NAME"]
        api_key = os.environ["API_KEY"]

        return ChatGptAdapter(endpoint, model, api_key)
