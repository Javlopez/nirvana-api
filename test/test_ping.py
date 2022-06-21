import falcon
from falcon import testing
import pytest

from api.app import app


@pytest.fixture
def client():
    return testing.TestClient(app)


def test_ping_handler(client):
    response = client.simulate_get('/ping')
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'ping'}
    assert response.json['ping'] == True
    assert response.status == falcon.HTTP_OK
