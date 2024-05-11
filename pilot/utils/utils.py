# utils/utils.py

import os
import copy
from jinja2 import Environment, FileSystemLoader

from const.llm import MAX_QUESTIONS, END_RESPONSE
from logger.logger import logger

prompts_path = os.path.join(os.path.dirname(__file__), '..', 'prompts')
file_loader = FileSystemLoader(prompts_path)
env = Environment(loader=file_loader)


def get_prompt(prompt_name: str, original_data=None) -> str:
    data = copy.deepcopy(original_data) if original_data is not None else {}

    get_prompt_components(data)

    logger.info(f"Getting prompt for {prompt_name}")

    # Load the template
    template = env.get_template(prompt_name)

    # Render the template with the provided data
    output = template.render(data)

    return output


def get_prompt_components(data):
    # This function reads and renders all prompts inside /prompts/components and returns them in dictionary

    # Create an empty dictionary to store the file contents.
    prompts_components = {}
    data.update({
        'MAX_QUESTIONS': MAX_QUESTIONS,
        'END_RESPONSE': END_RESPONSE
    })

    # Create a FileSystemLoader
    prompts_path = os.path.join(os.path.dirname(__file__), '..', 'prompts/components')
    file_loader = FileSystemLoader(prompts_path)

    # Create the Jinja2 environment
    env = Environment(loader=file_loader)

    # Get the list of template names
    template_names = env.list_templates()

    # For each template, load and store its content
    for template_name in template_names:
        # Get the filename without extension as the dictionary key.
        file_key = os.path.splitext(template_name)[0]

        # Load the template and render it with no variables
        file_content = env.get_template(template_name).render(data)

        # Store the file content in the dictionary
        prompts_components[file_key] = file_content

    return data.update(prompts_components)


def get_role_description(role: str) -> str:
    return get_prompt(f'role_descriptions/{role}.prompt')
