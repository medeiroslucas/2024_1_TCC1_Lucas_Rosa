import os

from helpers.adapters.terminal_adapter import TerminalAdapter


class TerminalAdapterProvider:

    @staticmethod
    def get_adapter() -> TerminalAdapter:
        return TerminalAdapter()
