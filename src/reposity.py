from src.models.recipe_model import recipe_model
from src.core.validator import validator
from src.core.abstract_model import abstract_model

class reposity:
    '''
    Репозиторий данных
    '''
    __data = {}
    __receipts: list[recipe_model] = []

    # Список рецептов
    @property
    def receipts(self):
        return self.__receipts

    # Репозиторий данных
    @property
    def data(self):
        return self.__data

    # Ключ для единиц измерения
    @staticmethod
    def range_key():
        return "range_model"

    # Ключ для групп
    @staticmethod
    def group_key():
        return "group_model"

    # Ключ для номенклатур
    @staticmethod
    def nomenclature_key():
        return "nomenclature_model"

    # Метод сохранения данных в __data по ключу key
    def append(self, key: str, value: abstract_model):
        validator.validate(value, abstract_model)
        validator.validate(key, str)
        if key not in self.data:
            self.data[key] = [value]
        else:
            self.data[key].append(value)
