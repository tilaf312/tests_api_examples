import pytest

from src.baseclasses.response import Response
from src.schemas.users import UserList


def test_get_users(get_users):
    """Проверка струтуры даныных по запросу юзеров и кода"""
    resp = Response(get_users())
    resp.validate(resp.response, UserList)
    resp.validate_status_code([200])


@pytest.mark.parametrize
def test_get_users_limit_offset_filtration(get_users):
    resp = Response(get_users())
