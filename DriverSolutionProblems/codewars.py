from utils.enums.EnumIdentifierTypeDriver import EnumIdentifierType

DRIVER_DICT = {
    'url_navagation': 'https://www.codewars.com/',
    'url_scrapper': 'https://www.codewars.com/users/[USER]/completed_solutions',
    'button_go_login': {
        "identifier": '//*[@id="header_section"]/ul/li[3]/a',
        "identifier_type": EnumIdentifierType.xpath,
        "tag":'a'
    },
    'login':{
        "user_email": {
            "identifier": '//*[@id="user_email"]',
            "identifier_type": EnumIdentifierType.xpath,
            "tag":'input'
        },
        "user_password": {
            "identifier": '//*[@id="user_password"]',
            "identifier_type": EnumIdentifierType.xpath,
            "tag":'input'
        },
        "submit_button": {
            "identifier": '//*[@id="new_user"]/button[2]',
            "identifier_type": EnumIdentifierType.xpath,
            "tag":'button'
        },
    },
    'solutions':{
        'blocks':{
            "identifier":'//*[@id="shell_content"]/div[5]/div/div[2]/div',
            "identifier_type":EnumIdentifierType.xpath,
            "tag":'div'
        },
        'quantity':{
            "identifier":'//*[@id="shell_content"]/div[5]/div/div[1]/ul/li[1]/a',
            "identifier_type":EnumIdentifierType.xpath,
            "tag":'a'
        }
    }
}