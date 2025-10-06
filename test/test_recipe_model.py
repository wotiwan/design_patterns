import unittest
from src.models.recipe_model import recipe_model
from src.models.nomenclature_model import nomenclature_model
from src.models.nomenclature_group_model import nomenclature_group_model
from src.models.range_model import range_model


class TestRecipeModel(unittest.TestCase):
    def setUp(self):
        self.group = nomenclature_group_model("Сырье")
        self.measure_unit = range_model.create_gramm()

        self.bread = nomenclature_model("Хлеб", self.group, self.measure_unit)
        self.butter = nomenclature_model("Масло сливочное", self.group, self.measure_unit)
        self.cheese = nomenclature_model("Сыр", self.group, self.measure_unit)

        self.recipe = recipe_model()
        self.recipe.name = "Бутерброд с маслом и сыром"

    def test_add_ingredient_success(self):
        """Добавление ингредиента должно работать корректно"""
        added = self.recipe.add_ingredient(self.bread, 2)
        self.assertTrue(added)
        self.assertEqual(len(self.recipe.ingredients), 1)

    def test_add_duplicate_ingredient_fails(self):
        """Повторное добавление того же ингредиента запрещено"""
        self.recipe.add_ingredient(self.butter, 10)
        added_again = self.recipe.add_ingredient(self.butter, 5)
        self.assertFalse(added_again)
        self.assertEqual(len(self.recipe.ingredients), 1)

    def test_add_step(self):
        """Добавление шагов приготовления"""
        self.recipe.steps = ["Намазать хлеб маслом.", "Положить сверху сыр."]
        self.assertEqual(len(self.recipe.steps), 2)

    def test_description_validation(self):
        """Проверка установки описания"""
        self.recipe.description = "Простой рецепт бутерброда"
        self.assertEqual(self.recipe.description, "Простой рецепт бутерброда")

    def test_factory_method_create_butter_cheese_sandwich(self):
        """Фабричный метод должен вернуть корректный рецепт"""
        recipe = recipe_model.create_butter_cheese_sandwich_recipe(
            self.bread, self.butter, self.cheese
        )
        self.assertEqual(recipe.name, "Бутерброд с маслом и сыром")
        self.assertEqual(len(recipe.ingredients), 3)
        self.assertTrue(any(n.name == "Хлеб" for n, _ in recipe.ingredients))


if __name__ == "__main__":
    unittest.main()
