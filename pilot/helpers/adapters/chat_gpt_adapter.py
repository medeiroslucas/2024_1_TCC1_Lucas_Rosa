from abc import ABC

import requests

from typing import List, Dict

from helpers.adapters.llm_adapter import LlmAdapter
from helpers.exceptions import ApiException
from logger.logger import logger


class ChatGptAdapter(LlmAdapter):
    API_CONNECT_TIMEOUT = 30
    API_READ_TIMEOUT = 300

    def __init__(self, endpoint: str, model: str, api_key: str, ):

        self.endpoint = endpoint
        self.model = model
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + api_key
        }

    def get_conversation_completion(self,
                                    messages: List[Dict],
                                    temperature: float = 0.7,
                                    n: int = 1,
                                    top_p: int = 1,
                                    presence_penalty: int = 0,
                                    frequency_penalty: int = 0,
                                    stream: bool = False) -> Dict:

        request_data = {
            'model': self.model,
            'n': n,
            'temperature': temperature,
            'top_p': top_p,
            'presence_penalty': presence_penalty,
            'frequency_penalty': frequency_penalty,
            'messages': messages,
            'stream': stream
        }

        response: requests.Response = self.send_request(request_data)

        if response.status_code != 200:
            logger.info(f'problem with request (status {response.status_code}): {response.text}')
            raise ApiException(f"API responded with status code: {response.status_code}. "
                               f"Response text: {response.text}", response=response)

        return self.extract_conversation_completion(response.json())

    def send_request(self, request_data: Dict, stream: bool = False) -> requests.Response:

        logger.info(f"Calling ChatGpt using endpoint: {self.endpoint} and model: {self.model}")
        logger.debug(f"Calling ChatGpt using endpoint: {self.endpoint}, model: {self.model} "
                     f"and data request: {request_data}")

        return requests.post(
            url=self.endpoint,
            headers=self.headers,
            json=request_data,
            stream=stream,
            timeout=(self.API_CONNECT_TIMEOUT, self.API_READ_TIMEOUT)
        )

    @staticmethod
    def extract_conversation_completion(response_json: Dict) -> Dict:
        return response_json["choices"][0]["message"]
