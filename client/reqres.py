from requests import request
from client.client import Client


class Reqres(Client):

    def __init__(self):
        self.path = "https://reqres.in/api/{path}"

    def get_users(self, params: dict):
        self.response = request(method='GET',
                                url=self.path.format(path='users'),
                                params=params)
        return self

    def get_user(self, user: int):
        self.response = request(method='GET',
                                url=self.path.format(path=f'users/{user}'))
        return self