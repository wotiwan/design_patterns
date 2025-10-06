from src.core.abstract_model import abstract_model
from src.core.validator import validator
from src.models.range_model import range_model
from src.models.nomenclature_group_model import nomenclature_group_model


"""Модель номенклатуры (продукта / ингредиента)"""
class nomenclature_model(abstract_model):
    __full_name: str = ""
    __group: nomenclature_group_model
    __measure_unit: range_model

    def __init__(self,
                 name: str = "",
                 group: nomenclature_group_model = None,
                 measure_unit: range_model = None):
        super().__init__()

        # self.name = name
        self.__group = group if group else nomenclature_group_model()
        self.__measure_unit = measure_unit if measure_unit else range_model.create_gramm()
        self.__full_name = name

    """Поле с полным именем номенклатуры"""
    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        full_name_length = 255  # max permitted length
        validator.validate(value, str, full_name_length)
        self.__full_name = value.strip()

    """Группа номенклатуры (например: 'Сырье', 'Продукт')"""
    @property
    def group(self) -> nomenclature_group_model:
        return self.__group

    @group.setter
    def group(self, value: nomenclature_group_model):
        validator.validate(value, nomenclature_group_model)
        self.__group = value

    """Единица измерения (например: грамм, литр, кг)"""
    @property
    def measure_unit(self) -> range_model:
        return self.__measure_unit

    @measure_unit.setter
    def measure_unit(self, value: range_model):
        validator.validate(value, range_model)
        self.__measure_unit = value

    # Фабричные методы
    @staticmethod
    def create_bread(group: nomenclature_group_model, measure_unit: range_model):
        validator.validate(group, nomenclature_group_model)
        validator.validate(measure_unit, range_model)
        return nomenclature_model("Хлеб", group, measure_unit)

    @staticmethod
    def create_butter(group: nomenclature_group_model, measure_unit: range_model):
        validator.validate(group, nomenclature_group_model)
        validator.validate(measure_unit, range_model)
        return nomenclature_model("Масло сливочное", group, measure_unit)

    @staticmethod
    def create_cheese(group: nomenclature_group_model, measure_unit: range_model):
        validator.validate(group, nomenclature_group_model)
        validator.validate(measure_unit, range_model)
        return nomenclature_model("Сыр", group, measure_unit)

    def __str__(self) -> str:
        return f"{self.name or self.full_name} ({self.measure_unit.name})"
