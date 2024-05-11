import platform
import questionary
import sys
from utils.style import style_config
from utils.print import remove_ansi_codes


def styled_get_input(question, style=None) -> str:
    """
    Ask the user a question and return the answer.

    NOTE: Use ask_user() instead of this function!
    Use styled_text() only if you don't want to trigger project.finish_loading()!
    """

    used_style = style if style is not None else style_config.get_style()
    question = remove_ansi_codes(question)  # Colorama and questionary are not compatible and styling doesn't work
    flush_input()
    response = questionary.text(question, style=used_style).unsafe_ask()  # .ask() is included here

    return response


def get_user_feedback():
    return questionary.text('How did GPT Pilot do? Were you able to create any app that works? '
                            'Please write any feedback you have or just press ENTER to exit: ',
                            style=style_config.get_style()).unsafe_ask()


def ask_user_to_store_init_prompt():
    return questionary.text('We would appreciate if you let us store your initial app prompt. '
                            'If you are OK with that, please just press ENTER',
                            style=style_config.get_style()).unsafe_ask()


def flush_input():
    """Flush the input buffer, discarding all that's in the buffer."""
    try:
        if platform.system() == 'Windows':
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()
        else:
            import termios
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    except (ImportError, OSError):
        pass
