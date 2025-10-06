from typing import Optional, List, Dict
from src.core.validator import validator
from src.models.recipe_model import recipe_model
from src.models.range_model import range_model
from src.models.nomenclature_model import nomenclature_model
from src.models.nomenclature_group_model import nomenclature_group_model
from src.reposity import reposity


"""Класс, наполняющий приложение эталонными объектами разных типов"""
class start_service:
    # Ссылка на экземпляр StartService (Singleton)
    __instance = None

    # Ссылка на объект Repository
    __repository: Optional[reposity] = reposity()

    def __init__(self):
        # Инициализация контейнеров данных
        self.data[reposity.range_key()] = dict()
        self.data[reposity.group_key()] = dict()
        self.data[reposity.nomenclature_key()] = dict()
        self.data[reposity.receipts] = list()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    """Словарь данных репозитория"""
    @property
    def data(self) -> dict:
        return self.__repository.data

    """Эталонные единицы измерения"""
    @property
    def measure_units(self) -> Dict[str, range_model]:
        return self.data[reposity.range_key()]

    """Метод генерации эталонных единиц измерения"""
    def __create_measure_units(self):
        names = reposity.range_key()

        gramm = range_model.create_gramm()
        kilo = range_model.create_kg()
        slice_unit = range_model.create("slice", 1)  # ломтик хлеба
        piece_unit = range_model.create("piece", 1)  # кусочек сыра
        butter_unit = range_model.create("spoon", 10, gramm)  # ложка масла

        if gramm.name not in self.measure_units:
            self.measure_units[gramm.name] = gramm
        if kilo.name not in self.measure_units:
            self.measure_units[kilo.name] = kilo
        if slice_unit.name not in self.measure_units:
            self.measure_units[slice_unit.name] = slice_unit
        if piece_unit.name not in self.measure_units:
            self.measure_units[piece_unit.name] = piece_unit
        if butter_unit.name not in self.measure_units:
            self.measure_units[butter_unit.name] = butter_unit

    """Эталонные группы номенклатуры"""
    @property
    def nomenclature_groups(self) -> Dict[str, nomenclature_group_model]:
        return self.data[reposity.group_key()]

    """Метод генерации эталонных групп номенклатуры"""

    def __create_nomenclature_groups(self):
        key = reposity.group_key()
        self.data[key] = {}

        groups = {
            "raw_material": "Сырье",
            "finished_goods": "Готовая продукция"
        }

        for code, name in groups.items():
            from src.models.nomenclature_group_model import nomenclature_group_model
            g = nomenclature_group_model()
            g.name = name
            self.data[key][code] = g

    """Список номенклатур"""

    @property
    def nomenclatures(self) -> Dict[str, nomenclature_model]:
        return self.data[reposity.nomenclature_key()]

    """Метод добавления номенклатур"""

    def __create_nomenclatures(self):
        # Получаем ключи для обращения к self.data
        group_key = reposity.group_key()
        range_key = reposity.range_key()

        # Получаем уже созданные группы и диапазоны
        groups = self.nomenclature_groups
        ranges = self.data[range_key]

        # Ссылки на группы
        raw_material = groups["raw_material"]
        finished_goods = groups["finished_goods"]

        # Создание номенклатур
        flour = nomenclature_model()
        flour.full_name = "Мука пшеничная"
        flour.group = raw_material
        flour.range = ranges["Гр."]

        bread = nomenclature_model()
        bread.full_name = "Хлеб"
        bread.group = finished_goods
        bread.range = ranges["piece"]

        butter = nomenclature_model()
        butter.full_name = "Масло сливочное"
        butter.group = raw_material
        butter.range = ranges["spoon"]

        cheese = nomenclature_model()
        cheese.full_name = "Сыр"
        cheese.group = raw_material
        cheese.range = ranges["piece"]

        # Добавляем в репозиторий
        self.nomenclatures["flour"] = flour
        self.nomenclatures["bread"] = bread
        self.nomenclatures["butter"] = butter
        self.nomenclatures["cheese"] = cheese

    def __create_recipes(self):
        bread = self.get_nomenclature("Хлеб")
        butter = self.get_nomenclature("Масло сливочное")
        cheese = self.get_nomenclature("Сыр")

        sandwich = recipe_model()
        sandwich.name = "Бутерброд с маслом и сыром"
        sandwich.description = "Простой и быстрый завтрак за 2 минуты."

        sandwich.add_ingredient(bread, 2)
        sandwich.add_ingredient(butter, 10)
        sandwich.add_ingredient(cheese, 20)

        sandwich.steps = [
            "Намазать хлеб сливочным маслом.",
            "Положить сверху кусочек сыра.",
            "При желании подогреть на сковороде или в тостере."
        ]

        self.recipes.append(sandwich)

    """Метод получения номенклатуры по имени"""

    def get_nomenclature(self, name: str) -> Optional[nomenclature_model]:
        validator.validate(name, str)
        for nom in self.nomenclatures.values():
            if nom.full_name == name:
                return nom
        return None

    """Список рецептов"""
    @property
    def recipes(self) -> List[recipe_model]:
        return self.data[reposity.receipts]

    """Метод добавления эталонных рецептов"""

    """Метод вызова генерации эталонных данных"""
    def start(self):
        self.__create_measure_units()
        self.__create_nomenclature_groups()
        self.__create_nomenclatures()
        self.__create_recipes()
