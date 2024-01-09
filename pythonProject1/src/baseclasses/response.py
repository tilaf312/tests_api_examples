from src.enums.global_enums import CustomErrors
from pydantic import ValidationError


class Response:
    def __init__(self, response):
        self.response = response.json()
        self.status_code = response.status_code
        self.data = self.response.get('data')
        self.meta = self.response.get('meta')

    def get_data_count(self):
        """Получить количество объектов из data"""
        return len(self.data)

    @staticmethod
    def validate(obj, schema):
        """ Валидация структуры ответа
        :param obj: объект валидации
        :param schema: схема по которой валидируем(pydantic)"""
        try:
            if isinstance(obj, list):
                for item in obj:
                    schema.model_validate(item)
            else:
                schema.model_validate(obj)
        except ValidationError:
            raise AssertionError(CustomErrors.WRONG_VALIDATION_OBJECT.value)

    def validate_status_code(self, status_code):
        """ Проверка кода статуса
        :param status_code: ожидаемый код """
        assert self.status_code in status_code, CustomErrors.WRONG_RESPONSE_CODE.value

    def check_param_in_meta(self, param_name, param_value):
        """ Базовые проверки с параметром в meta-теге
        :param param_name: Название параметра
        :param param_value: Ожидаемое значение параметра"""

        getted_value = self.meta.get(param_name)
        assert getted_value is not None, CustomErrors.WRONG_OBJECT_NOT_FOUND.value
        assert getted_value == param_value, CustomErrors.WRONG_OBJECT_NOT_FOUND.value

    def check_limit_offset_filtration(self, limit, offset, key):
        """ Проверка офсета в списке возвращаемых данных
        :param limit: параметр количества выдаваемых данных
        :param offset: параметр отсупа
        :param key: ключ по котормоу проверяем offset(уникальный ид)"""

        self.check_param_in_meta('limit', limit)
        self.check_param_in_meta('offset', offset)
        getted_data_count = self.get_data_count()
        total_param = self.meta.get('total')
        if limit == 0:
            assert getted_data_count == 0, CustomErrors.WRONG_COUNT_OBJECTS.value
        elif limit > total_param and offset == 0:
            assert getted_data_count == total_param, CustomErrors.WRONG_COUNT_OBJECTS.value
        elif limit > total_param and offset != 0:
            assert getted_data_count + offset == total_param, CustomErrors.WRONG_COUNT_OBJECTS.value
        else:
            assert limit == getted_data_count, CustomErrors.WRONG_COUNT_OBJECTS.value
            assert offset + 1 == self.data[0].get(key), CustomErrors.WRONG_OFFSET_DATA.value

    @staticmethod
    def check_status_company(obj, status, key):
        if isinstance(obj, list):
            for i in obj:
                assert i.get(key) == status
        else:
            assert obj.get(key) == status
