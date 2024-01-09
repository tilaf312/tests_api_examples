import pytest
import requests
from configuration import SERVICE_URL


def _get_companies(path='', headers=None, **kwargs):
    resp = requests.get(SERVICE_URL + 'api/companies' + path, params=kwargs, headers=headers)
    return resp


@pytest.fixture
def get_companies():
    return _get_companies
