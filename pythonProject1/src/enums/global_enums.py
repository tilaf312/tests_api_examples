from src.enums.custom_enum_class import CustomEnum


class CustomErrors(CustomEnum):
    WRONG_RESPONSE_CODE = 'Ожидаемый статус код отличается от фактического'
    WRONG_VALIDATION_OBJECT = 'Ошибка при валидации объекта'
    WRONG_COUNT_OBJECTS = 'Ожидаемое количество объектов в запросе отличается от фактического'
    WRONG_OBJECT_NOT_FOUND = 'Объект не найден'
    WRONG_PARAM_IS_DIFFERENT = 'Ожидаемое значения параметра отличается от фактического'
    WRONG_OFFSET_DATA = 'Неверный offset у списка данных'
