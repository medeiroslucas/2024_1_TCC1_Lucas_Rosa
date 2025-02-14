from helpers.agents.agent import Agent
from const.roles import Roles


class TechnicalWriter(Agent):

    def __init__(self):
        super().__init__(Roles.TECHNICAL_WRITER.value)
