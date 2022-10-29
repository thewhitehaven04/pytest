import json
from requests import Response


class Client:

    def __init__(self) -> None:
        self.response: Response

    def get_str(self) -> str:
        return self.response.text

    def get_json(self) -> dict:
        return json.loads(self.get_str())