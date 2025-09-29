from src.core.abstract_model import abstract_model
from src.core.validator import validator

class range_model(abstract_model):
    __conversion_ratio: int

    def __init__(self, name: str, conversion_ratio: int, base_range = None):
        super().__init__()
        self.name = name # validator.validate(name, str)
        self.__conversion_ratio = conversion_ratio
        self.__base_range: range_model = base_range

    # conversation_ratio getter
    @property
    def conversation_ratio(self) -> int:
        return self.__conversion_ratio

    @conversation_ratio.setter
    def conversation_ratio(self, value: int):
        validator.validate(value, int)
        self.__conversion_ratio = value

    # base_range getter, returns name
    @property
    def base_range(self):
        return self.__base_range

    @base_range.setter
    def base_range(self, value):
        validator.validate(value, range_model)
        self.__base_range = value