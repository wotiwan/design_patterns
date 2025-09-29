import uuid
from abc import ABC
from src.core.validator import validator

class abstract_model(ABC):

    def __init__(self):
        self.__name: str = ""
        self.__unique_id: str = uuid.uuid4().hex

    @property
    def unique_code(self) -> str:
        return self.__unique_id

    @unique_code.setter
    def unique_code(self, value: str):
        validator.validate(value, str)
        self.__unique_id = value.strip()

    def __eq__(self, other):
        return self.__unique_id == other.__unique_id

    # name setter and getter
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        validator.validate(value, str, 50)  # Каждый раз создаём валидатор?
        self.__name = value.strip()