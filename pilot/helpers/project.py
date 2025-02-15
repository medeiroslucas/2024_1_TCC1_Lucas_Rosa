from helpers.agents.tech_lead import TechLead
# from helpers.agents.developer import Developer
from helpers.agents.architect import Architect
from helpers.agents.product_owner import ProductOwner
from helpers.agents.technical_writer import TechnicalWriter
from prompts.prompts import ask_user


class Project:
    def __init__(self,
                 project_name: str,
                 product_owner: ProductOwner,
                 architect: Architect,
                 developer,
                 technical_writer: TechnicalWriter,
                 tech_lead: TechLead):
        """
        Initialize a project.

        """
        self.project_name = project_name
        self.product_owner = product_owner
        self.architect = architect
        self.developer = developer
        self.technical_writer = technical_writer
        self.tech_lead = tech_lead

    def start(self):

        main_description, high_level_specs = self.product_owner.get_project_description()

        architecture = self.architect.get_architecture(main_description, high_level_specs)
        end_to_end_use_cases = self.architect.get_end_2_end_use_cases()
        use_cases_diagrams = self.architect.get_use_cases_diagram()
        architecture_diagram = self.architect.get_architecture_diagram()
        development_plan = self.tech_lead.get_development_plan(main_description, high_level_specs, architecture, end_to_end_use_cases)

        print("\n## Architecture\n")
        print(architecture)
        print("\n## End to end use cases\n")
        print(end_to_end_use_cases)
        print("\n## Use case diagrams\n")
        print(use_cases_diagrams)
        print("\n## Architecture diagram\n")
        print(architecture_diagram)
        print("\n## Development Plan")
        print(development_plan)
        return
