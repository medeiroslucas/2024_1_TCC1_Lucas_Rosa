from helpers.agents.spec_writer import SpecWriter
from helpers.agents.agent import Agent
from logger.logger import logger
from prompts.prompts import ask_user
from const.roles import Roles


class ProductOwner(Agent):
    def __init__(self, spec_writer: SpecWriter):
        super().__init__(Roles.PRODUCT_OWNER.value)
        self.spec_writer = spec_writer

    def get_project_description(self) -> (str, str):

        main_description = self.get_project_main_description()
        high_level_specs = self.spec_writer.create_spec(main_description)

        return main_description, high_level_specs

    @staticmethod
    def get_project_main_description() -> str:
        question = 'Describe your app in as much detail as possible.'
        description = ask_user(question)

        if description is None:
            print("No input provided!")
            return ''

        logger.info(f"Initial App description done: {description}")

        return description
