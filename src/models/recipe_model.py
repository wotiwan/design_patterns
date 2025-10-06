from src.core.abstract_model import abstract_model
from src.models.range_model import range_model
from src.models.nomenclature_model import nomenclature_model
from src.core.validator import validator, argument_exception


class recipe_model(abstract_model):

    def __init__(self, _name: str = "Новый рецепт", _number_of_servings: int = 1, _ingredients: list[tuple[nomenclature_model, int]] = None,
                 _steps: list[str] = None,
                 _cooking_length: range_model = range_model()):
        super().__init__()
        self.name = _name
        self.__servings_count: int = _number_of_servings
        self.__ingredients: list[tuple[nomenclature_model, int]] = _ingredients or []
        self.__steps: list[str] = _steps or []
        self.__cooking_time: range_model = _cooking_length

    # Количество порций
    @property
    def servings_count(self):
        return self.__servings_count

    @servings_count.setter
    def servings_count(self, value: int):
        validator.validate(value, int)
        if value <= 0:
            raise argument_exception("Неверный аргумент!")
        self.__servings_count = value

    # Время приготовления
    @property
    def cooking_time(self):
        return self.__cooking_time

    @cooking_time.setter
    def cooking_time(self, value: range_model):
        validator.validate(value, range_model)
        self.__cooking_time = value

    # Список ингредиентов
    @property
    def ingredients(self) -> list[tuple[nomenclature_model, int]]:
        return self.__ingredients

    def add_ingredient(
            self,
            nomenclature: nomenclature_model,
            count: int
    ) -> bool:
        validator.validate(nomenclature, nomenclature_model)
        validator.validate(count, int)

        for nom, _ in self.ingredients:
            if nom == nomenclature or nom.name == nomenclature.name:
                return False

        # Добавляем если ещё нет в словаре
        self.__ingredients.append((nomenclature, count))
        return True

    # Пошаговый список инструкций
    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, value: list):
        validator.validate(value, list)
        self.__steps = value

    """Фабричный метод для создания рецепта бутерброда с маслом и сыром"""

    @staticmethod
    def create_butter_cheese_sandwich_recipe(
            bread_nomenclature: nomenclature_model,
            butter_nomenclature: nomenclature_model,
            cheese_nomenclature: nomenclature_model,
    ):
        validator.validate(bread_nomenclature, nomenclature_model)
        validator.validate(butter_nomenclature, nomenclature_model)
        validator.validate(cheese_nomenclature, nomenclature_model)

        recipe = recipe_model()
        recipe.name = "Бутерброд с маслом и сыром"
        recipe.description = "Простой и быстрый рецепт для завтрака."

        recipe.add_ingredient(bread_nomenclature, 2)  # ломтика хлеба
        recipe.add_ingredient(butter_nomenclature, 15)  # грамм масла
        recipe.add_ingredient(cheese_nomenclature, 20)  # грамм сыра

        return recipe
