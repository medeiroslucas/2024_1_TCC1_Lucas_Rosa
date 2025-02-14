from typing import List, Dict

from helpers.adapters.llm_adapter import LlmAdapter

from utils.utils import get_prompt
from logger.logger import logger


class ConversationalAgent:
    messages: List[Dict[str, str]] = []

    def __init__(self, role: str, role_description: str, llm_adapter: LlmAdapter):
        self.role = role
        self.llm_adapter = llm_adapter
        self.llm_role = llm_adapter.llm_role
        self.log_to_user = True
        self.append_message({"role": self.llm_role, "content": role_description})

    def append_message(self, message: Dict[str, str]):
        self.messages.append(message)

    def send_messages(self, temperature: float = 0.7) -> Dict:
        return self.llm_adapter.get_conversation_completion(self.messages, temperature=temperature)

    def append_prompt_to_messages(self, prompt_path, prompt_variables: Dict = None):
        if prompt_path:
            prompt = get_prompt(prompt_path, prompt_variables)
            logger.info(f'\n>>>>>>>>>> User Prompt >>>>>>>>>>\n{prompt}\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            self.append_message({"role": "user", "content": prompt})

    def append_user_input_to_messages(self, user_input):
        self.append_message({"role": "user", "content": user_input})
