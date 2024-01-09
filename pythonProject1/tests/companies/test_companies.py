import pytest

from src.baseclasses.response import Response
from src.schemas.companies import Company, CompanyList
from src.schemas.error import HTTPValidationError
from src.enums.company_enums import CompanyStatuses
from src.enums.company_enums import CompanyDescriptionLang, WrongCompanyDescriptionLang


def test_get_companies(get_companies):
    """ Проверка струтуры даныных по запросу компаний и кода """
    resp = Response(get_companies())
    resp.validate(resp.response, CompanyList)
    resp.validate_status_code([200])


@pytest.mark.parametrize('limit', [1, 10, 0])
@pytest.mark.parametrize('offset', [0, 1, 10])
def test_get_companies_filtration_limit_offset(get_companies, limit, offset):
    """ Проверка фильтрации с параметрами limit и offset """
    resp = Response(get_companies(limit=limit, offset=offset))
    resp.check_limit_offset_filtration(limit, offset, 'company_id')


@pytest.mark.parametrize('status', CompanyStatuses.list())
def test_get_companies_filtration_status(get_companies, status):
    """ Проверка фильтрации с параметрами limit и offset """
    resp = Response(get_companies(status=status))
    resp.check_status_company(resp.data, status, 'company_status')


@pytest.mark.parametrize('company_id, expected', [
    ('1', 'find'),
    ('15', 'unfind'),
    ('asd', 'unfind'),
    ('!@$%#^asd', 'unfind')
])
def test_get_company(get_companies, company_id, expected):
    resp = Response(get_companies(path=f'/{company_id}'))
    if expected == 'find':
        resp.validate(resp.response, Company)
        resp.validate_status_code([200])
    elif expected == 'unfind':
        resp.validate(resp.response, HTTPValidationError)
        resp.validate_status_code([404, 422])


@pytest.mark.parametrize('lang', CompanyDescriptionLang.list())
def test_description_lang(get_companies, lang):
    resp = Response(get_companies(path=f'/1', headers={'Accept-Language': lang}))
    resp.validate_status_code([200])
    resp.validate(resp.response, Company)


@pytest.mark.parametrize('lang', WrongCompanyDescriptionLang.list())
def test_description_wrong_lang(get_companies, lang):
    resp = Response(get_companies(path=f'/1', headers={'Accept-Language': lang}))
    resp.validate_status_code([200])
    resp.validate(resp.response, Company)
