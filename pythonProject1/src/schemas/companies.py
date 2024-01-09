from pydantic import BaseModel
from src.enums.company_enums import CompanyStatuses, CompanyDescriptionLang
from src.schemas.meta import Meta


class CompanyDescription(BaseModel):
    translation_lang: CompanyDescriptionLang
    translation: str


class Company(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: CompanyStatuses
    description: str = None
    description_lang: list[CompanyDescription] = None


class CompanyList(BaseModel):
    data: list[Company]
    meta: Meta
