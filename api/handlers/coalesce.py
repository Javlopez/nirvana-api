"""Coalesce handler"""
import json
import math

import falcon

from api.data.data import Data
from api.exceptions.exceptions import InvalidClientResponseException
from api.service.client import Client


class Coalesce:
    """Coalesce handler"""

    API1 = 'http://0.0.0.0:8000/api1/v1/'
    API2 = 'http://0.0.0.0:8000/api2/v1/'
    API3 = 'http://0.0.0.0:8000/api3/v1/'

    def __init__(self, client: Client):
        self.client = client

    def call_member_api(self, api) -> Data:
        try:
            data = self.client.get(api)
            j = json.loads(data)
            return Data(**j)
        except Exception:
            raise InvalidClientResponseException("The json load is not valid")

    def on_get(self, req, resp):
        """Get handler for ping endpoint"""
        try:
            collection_data = [self.call_member_api(self.API1), self.call_member_api(self.API2),
                               self.call_member_api(self.API3)]

            deductible = 0
            stop_loss = 0
            oop_max = 0
            items = len(collection_data)
            for data in collection_data:
                deductible += data.deductible
                stop_loss += data.stop_loss
                oop_max += data.oop_max

            resp.media = {
                "deductible": math.trunc(deductible / items),
                "stop_loss": math.trunc(stop_loss / items),
                "oop_max": math.trunc(oop_max / items),
            }
            resp.status = falcon.HTTP_200
        except Exception:
            # Normally you would also log the error.
            raise falcon.HTTPInternalServerError()
