import json

import requests

from api.exceptions.exceptions import ApiClientException


class Client:

    def get(self, api) -> str:
        response = requests.get(f"{api}")
        if response.status_code == 200:
            return json.dumps(response.json())

        raise ApiClientException(f"The api has is not able to call {api} endpoint")

