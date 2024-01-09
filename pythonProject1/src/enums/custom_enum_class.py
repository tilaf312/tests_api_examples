from enum import Enum


class CustomEnum(Enum):
    @classmethod
    def list(cls) -> list:
        return list(map(lambda c: c.value, cls))