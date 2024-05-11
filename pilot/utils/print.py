import re


def remove_ansi_codes(s: str) -> str:
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    # Check if the input is a string
    if isinstance(s, str):
        return ansi_escape.sub('', s)
    else:
        # If the input is not a string, return the input as is
        return s
