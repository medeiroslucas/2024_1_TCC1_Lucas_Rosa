from abc import ABC, abstractmethod
from typing import Dict

import requests


class LlmAdapter(ABC):

    @abstractmethod
    def send_request(self, args, **kwarg) -> requests.Response:
        raise NotImplementedError

    @abstractmethod
    def get_conversation_completion(self, args, **kwargs) -> Dict:
        raise NotImplementedError
