from crawler.BaseCrawler import BaseCrawler
from DriverSolutionProblems.codewars import DRIVER_DICT
from DTO.UserDTO import UserDTO
from utils.StringHelper.BaseStringHelper import BaseStringHelper

class SolutionProblemCrawler(BaseCrawler):
    def __init__(self, url_login, url_scrapper, browser):
        super().__init__(url_login, url_scrapper, browser)
    
    def start_json_driver(self, user_dto:UserDTO):
        self.url_navagation = None if 'url_navagation' not in DRIVER_DICT else DRIVER_DICT['url_navagation']
        self.login_driver = None if 'login' not in DRIVER_DICT else DRIVER_DICT['login']
        self.solutions = None if 'solutions' not in DRIVER_DICT else DRIVER_DICT['solutions']
        self.button_go_login = None if 'button_go_login' not in DRIVER_DICT else DRIVER_DICT['button_go_login']
        self.url_scrapper = None if 'url_scrapper' not in DRIVER_DICT else DRIVER_DICT['url_scrapper']

        if self.url_scrapper:
            string_helper:BaseStringHelper
            string_helper = BaseStringHelper()
            self.url_scrapper = string_helper.replace_string(
                self.url_scrapper,
                '[USER]',
                user_dto.nickname
            )
        
    def create_solution_dto(self, user):
        pass
    
    def get_solutions(self, user_dto:UserDTO):
        blocks_driver = self.solutions['blocks']
        blocks_solution = self._find_element_by(
            identifier=blocks_driver['identifier'],
            identifier_type=blocks_driver['identifier_type'],
            is_multiple = True
        )

    def save_solutions_on_db(self, solutions_dto):
        pass

    def main(self, users):
        if not users:
            return
        
        self.start_driver()
        
        for user in users:
            user_dto:UserDTO
            user_dto = UserDTO(user)

            self.start_json_driver(user_dto)
            self.driver.get(self.url_navagation)

            self.login(
                user_password = user_dto.password,
                user_email = user_dto.email,
                login_driver = self.login_driver,
                button_go_login = self.button_go_login
            )

            self.driver.get(self.url_scrapper)

            solutions_dto = self.get_solutions(user_dto)
            self.save_solutions_on_db(solutions_dto)
            
            


            


    