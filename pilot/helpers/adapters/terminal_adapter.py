from abc import ABC

import requests

from typing import List, Dict

from helpers.adapters.llm_adapter import LlmAdapter
from helpers.exceptions import ApiException
from logger.logger import logger


class TerminalAdapter(LlmAdapter):
    llm_role = None

    def get_conversation_completion(self,
                                    messages: List[Dict],
                                    temperature: float = 0.7,
                                    stream: bool = False) -> Dict:

        print("******************************************************************************************************")
        print("**************Copy and paste the following prompt on your chat, then paste the response **************")
        print("******************************************************************************************************")

        output = ""
        for message in messages:
            output += message.get("content")

        print(output)

        print("******************************************************************************************************")
        print("**************                        END (hit ctrl+d after pasting)                    **************")
        print("******************************************************************************************************")

        response = []
        try:
            while True:
                response.append(input())
        except EOFError:
            pass
        response = "\n".join(response)

        return {
            "role": "assistant",
            "content": response
        }

    def send_request(self, request_data: Dict, stream: bool = False) -> requests.Response:
        pass

    @staticmethod
    def extract_conversation_completion(response_json: Dict) -> Dict:
        return response_json["choices"][0]["message"]

# I want to create a chat app. An user must be able to login with an username, search other user by his username and start a chat
