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

        print("**********************************************")
        print(architecture)
        print("----------------------------------------------")

        development_plan = self.tech_lead.get_development_plan(main_description, high_level_specs, architecture)
        # self.developer.setup_environment(self.project_name)
        # self.developer.start_coding(self.project_name,
        #                             main_description,
        #                             high_level_specs,
        #                             architecture,
        #                             development_plan)


        print(development_plan)
        print("**********************************************")
        return
