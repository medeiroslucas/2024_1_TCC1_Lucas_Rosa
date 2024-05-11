# prompts/prompts.py
from utils.style import color_white_bold
from utils.questionary import styled_get_input
from logger.logger import logger


def ask_user(question: str, require_some_input=True, hint: str = None) -> str:
    while True:
        if hint is not None:
            print(color_white_bold(hint) + '\n')
        answer = styled_get_input(question)

        logger.info('Q: %s', question)
        logger.info('A: %s', answer)

        if answer is None:
            print("Exiting application.")
            exit(0)

        if answer.strip() == '' and require_some_input:
            print("No input provided! Please try again.")
            continue
        else:
            return answer
