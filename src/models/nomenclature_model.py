from src.core.abstract_model import abstract_model
from src.core.validator import validator

from src.models.range_model import range_model
from src.models.nomenclature_group_model import nomenclature_group_model

class nomenclature_model(abstract_model):
    __full_name: str = ""
    __nomenclature_group: nomenclature_group_model
    __range: range_model

    def __init__(self):
        super().__init__()
        self.__default()

    def __default(self):
        self.__nomenclature_group = nomenclature_group_model()
        self.__range = range_model("Г", 1000)

    # name setter and getter
    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        full_name_length = 255 # max permitted length
        validator.validate(value, str, full_name_length)
        self.__full_name = value.strip()