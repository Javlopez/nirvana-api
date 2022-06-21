import falcon
from falcon import testing
import pytest

from api.app import app


@pytest.fixture
def client():
    return testing.TestClient(app)


def test_mock_api_handler(client):
    response = client.simulate_get('/api1/v1/')
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'deductible', 'stop_loss', 'oop_max'}
    assert response.json['deductible'] > 0
    assert response.json['stop_loss'] > 0
    assert response.json['oop_max'] > 0
    assert response.status == falcon.HTTP_OK
