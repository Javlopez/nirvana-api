import falcon

from api.handlers.mock_api import MockApi
from api.handlers.ping import Ping
from api.handlers.coalesce import Coalesce
from api.service.client import Client


c = Client()
app = application = falcon.App()
ping_handler = Ping()
coalesce_handler = Coalesce(c)
app.add_route('/ping', ping_handler)
app.add_route('/coalesce', coalesce_handler)

# simulate as external apis
mock_api_handler = MockApi()
app.add_route('/api1/v1/', mock_api_handler)
app.add_route('/api2/v1/', mock_api_handler)
app.add_route('/api3/v1/', mock_api_handler)
