# main.py
try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError('Python environment for GPT Pilot is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()

import traceback

from helpers.agents.architect import Architect
# from helpers.agents.developer import Developer
from helpers.agents.tech_lead import TechLead
from helpers.agents.technical_writer import TechnicalWriter
from prompts.prompts import ask_user

from utils.style import color_red
from helpers.project import Project
from helpers.agents.product_owner import ProductOwner
from helpers.agents.spec_writer import SpecWriter

from helpers.exceptions import ApiException, TokenLimitError


def get_product_owner() -> ProductOwner:
    spec_writer: SpecWriter = get_spec_writer()
    return ProductOwner(spec_writer)


def get_spec_writer() -> SpecWriter:
    return SpecWriter()


def get_architect() -> Architect:
    return Architect()


# def get_developer() -> Developer | None:
#     return None


def get_tech_lead() -> TechLead:
    return TechLead()


def get_technical_writer() -> TechnicalWriter:
    return TechnicalWriter()


if __name__ == "__main__":
    ask_feedback = True
    run_exit_fn = True

    product_owner: ProductOwner = get_product_owner()
    architect: Architect = get_architect()
    developer = None
    technical_writer: TechnicalWriter = get_technical_writer()
    tech_lead: TechLead = get_tech_lead()

    try:

        project_name = ask_user('What is the project name?')

        project: Project = Project(project_name, product_owner, architect, developer, technical_writer, tech_lead)
        started = project.start()

    except (ApiException, TokenLimitError) as err:

        run_exit_fn = False
        if isinstance(err, TokenLimitError):
            print(color_red(
                "We sent too large request to the LLM, resulting in an error. "
                "This is usually caused by including framework files in an LLM request. "
            ))

    except Exception as err:
        print(color_red('---------- GPT PILOT EXITING WITH ERROR ----------'))
        print(err)
        traceback.print_exc()
        print(color_red('--------------------------------------------------'))
        ask_feedback = False
