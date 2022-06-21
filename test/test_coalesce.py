import json
from unittest.mock import Mock, patch

import falcon
from falcon import testing
import pytest

from api.app import app
from api.handlers.coalesce import Coalesce


@pytest.fixture
def client_with_invalid_response():
    mock = Mock()
    mock.get.side_effect = [
        'x data',
        '{"deductible": 1200, "stop_loss": 13000, "oop_max": 6000}',
        '{"deductible": 1000, "stop_loss": 10000, "oop_max": 6000}']
    coalesce_handler = Coalesce(mock)
    app.add_route('/coalesce', coalesce_handler)
    return testing.TestClient(app)


@pytest.fixture
def client():
    mock = Mock()
    mock.get.side_effect = [
        '{"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}',
        '{"deductible": 1200, "stop_loss": 13000, "oop_max": 6000}',
        '{"deductible": 1000, "stop_loss": 10000, "oop_max": 6000}']
    coalesce_handler = Coalesce(mock)
    app.add_route('/coalesce', coalesce_handler)
    return testing.TestClient(app)


def test_coalesce_handler(client):
    response = client.simulate_get('/coalesce')
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'deductible', 'stop_loss', 'oop_max'}
    assert response.json['deductible'] == 1066
    assert response.json['stop_loss'] == 11000
    assert response.json['oop_max'] == 5666
    assert response.status == falcon.HTTP_OK


def test_invalid_response_from_client(client_with_invalid_response):
    response = client_with_invalid_response.simulate_get('/coalesce')
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'title'}
    assert response.json['title'] == '500 Internal Server Error'
    assert response.status == falcon.HTTP_INTERNAL_SERVER_ERROR
