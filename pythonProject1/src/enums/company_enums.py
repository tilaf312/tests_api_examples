from src.enums.custom_enum_class import CustomEnum


class CompanyStatuses(CustomEnum):
    """Статусы компаний"""
    ACTIVE = 'ACTIVE'
    BANKRUPT = 'BANKRUPT'
    CLOSED = 'CLOSED'


class CompanyDescriptionLang(CustomEnum):
    EN = 'EN'
    RU = 'RU'
    PL = 'PL'
    UA = 'UA'


class WrongCompanyDescriptionLang(CustomEnum):
    FR = 'FR'
    NA = 'NA'
