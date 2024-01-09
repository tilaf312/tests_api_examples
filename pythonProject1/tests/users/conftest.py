import pytest
import requests
from configuration import SERVICE_URL


def _get_users(path='', headers=None, **kwargs):
    resp = requests.get(SERVICE_URL + 'api/users' + path, params=kwargs, headers=headers)
    return resp


@pytest.fixture
def get_users():
    return _get_users
