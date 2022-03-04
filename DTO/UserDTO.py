from .BaseDTO import BaseDTO

class UserDTO(BaseDTO):
    email:str
    password:str
    nickname:str
    def __init__(self, data:dict) -> None:
        super().__init__()

        self.email = None if 'email' not in data else data['email']
        self.password = None if 'password' not in data else data['password']
        self.nickname = None if 'nickname' not in data else data['nickname']
