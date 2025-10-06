from src.core.abstract_model import abstract_model
from src.core.validator import validator

class range_model(abstract_model):
    __conversion_ratio: int
    __base_range: str
    __name: str

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        validator.validate(value, str)
        self.__name = value.strip()

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


    @staticmethod
    def create_gramm():
        item = range_model()
        item = item.create("Гр.", 1)
        return item

    @staticmethod
    def create_kg():
        item = range_model()
        item = item.create("Кг.", 1000, item.create_gramm())
        return item

    @staticmethod
    def create_piece():
        """Создаёт единицу измерения 'Штука'"""
        item = range_model()
        item = item.create("штука", 1)
        return item

    @staticmethod
    def create_milliliter():
        """Создаёт единицу измерения 'Мл.'"""
        item = range_model()
        item = item.create("Мл.", 1)
        return item

    @staticmethod
    def create_liter():
        """Создаёт единицу измерения 'Литр'"""
        item = range_model()
        base = range_model.create_milliliter()
        item = item.create("Л.", 1000, base)
        return item

    @staticmethod
    def create(name: str, conversion_ratio: int, base_range=None):
        item = range_model()
        item.name = name
        item.conversion_ratio = conversion_ratio
        if base_range is not None:
            validator.validate(base_range, range_model)
            item.base_range = base_range
        return item