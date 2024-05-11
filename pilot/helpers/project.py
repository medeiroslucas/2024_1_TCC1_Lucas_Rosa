from helpers.agents.tech_lead import TechLead
from helpers.agents.developer import Developer
from helpers.agents.architect import Architect
from helpers.agents.product_owner import ProductOwner
from helpers.agents.technical_writer import TechnicalWriter


class Project:
    def __init__(self,
                 product_owner: ProductOwner,
                 architect: Architect,
                 developer: Developer,
                 technical_writer: TechnicalWriter,
                 tech_lead: TechLead):
        """
        Initialize a project.

        """
        self.product_owner = product_owner
        self.architect = architect
        self.developer = developer
        self.technical_writer = technical_writer
        self.tech_lead = tech_lead

    def start(self):

        main_description, high_level_specs = self.product_owner.get_project_description()

        architecture = self.architect.get_architecture(main_description, high_level_specs)
        return

    # def finish(self):
    #     """
    #     Finish the project.
    #     """
    #     while True:
    #         feature_description = ''
    #         if not self.features_to_load:
    #             self.finish_loading()
    #
    #         self.previous_features = get_features_by_app_id(self.args['app_id'])
    #         if not self.skip_steps:
    #             print('', type='verbose', category='pythagora')
    #             if self.run_command and self.check_ipc():
    #                 print(self.run_command, type='run_command')
    #             feature_description = ask_user(self, "Project is finished! Do you want to add any features or changes? "
    #                                                  "If yes, describe it here and if no, just press ENTER",
    #                                            require_some_input=False)
    #
    #             if feature_description == '' or feature_description == 'continue':
    #                 return
    #
    #             print('', type='verbose', category='agent:tech-lead')
    #             self.tech_lead.create_feature_plan(feature_description)
    #
    #         # loading of features
    #         else:
    #             num_of_features = len(self.features_to_load)
    #
    #             # last feature is always the one we want to load
    #             current_feature = self.features_to_load[-1]
    #             self.tech_lead.convo_feature_plan.messages = current_feature['messages'] + [{"role": "assistant", "content": current_feature['llm_response']['text']}]
    #             target_id = current_feature['id']
    #             self.cleanup_list('tasks_to_load', target_id)
    #             self.cleanup_list('dev_steps_to_load', target_id)
    #
    #             # if there is feature_summary.prompt in remaining dev steps it means feature is fully done
    #             # finish loading and ask to add another feature or finish project
    #             feature_summary_dev_step = next((el for el in reversed(self.dev_steps_to_load) if 'feature_summary.prompt' in el.get('prompt_path', '')), None)
    #             if feature_summary_dev_step is not None:
    #                 self.cleanup_list('dev_steps_to_load', feature_summary_dev_step['id'])
    #                 self.finish_loading()
    #                 print(f'loaded {num_of_features} features')
    #                 continue
    #
    #
    #             print(f'Loaded {num_of_features - 1} features!')
    #             print(f'Continuing feature #{num_of_features}...')
    #             self.development_plan = json.loads(current_feature['llm_response']['text'])['plan']
    #             feature_description = current_feature['prompt_data']['feature_description']
    #             self.features_to_load = []
    #
    #         self.current_feature = feature_description
    #         self.developer.start_coding('feature')
    #         print('', type='verbose', category='agent:tech-lead')
    #         self.tech_lead.create_feature_summary(feature_description)
