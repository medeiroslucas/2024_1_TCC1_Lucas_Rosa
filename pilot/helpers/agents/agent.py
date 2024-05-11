from utils.utils import get_role_description


class Agent:
    def __init__(self, role: str):
        self.role = role
        self.role_description = get_role_description(role)
