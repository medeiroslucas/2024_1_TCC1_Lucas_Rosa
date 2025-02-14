import os

from helpers.adapters.anthropic_adapter import AnthropicAdapter


class AnthropicAdapterProvider():

    @staticmethod
    def get_anthropic_adapter() -> AnthropicAdapter:
        endpoint = os.environ["ANTHROPIC_ENDPOINT"]
        model = os.environ["ANTHROPIC_MODEL_NAME"]
        api_key = os.environ["ANTHROPIC_API_KEY"]

        return AnthropicAdapter(endpoint, model, api_key)