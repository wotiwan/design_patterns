import unittest
from src.start_service import start_service
from src.models.range_model import range_model
from src.models.nomenclature_group_model import nomenclature_group_model
from src.models.nomenclature_model import nomenclature_model
from src.models.recipe_model import recipe_model
from src.reposity import reposity


class TestStartService(unittest.TestCase):
    def setUp(self):
        self.service = start_service()
        self.service.start()  # инициализация эталонных данных
        self.repo_data = self.service.data

    def test_measure_units_created(self):
        """Должны создаться базовые единицы измерения"""
        mu_data = self.service.measure_units
        self.assertTrue(len(mu_data) > 0)
        self.assertTrue(any("Гр." in mu_data))
        self.assertIsInstance(next(iter(mu_data.values())), range_model)

    def test_nomenclature_groups_created(self):
        """Должны создаться базовые группы номенклатуры"""
        groups = self.service.nomenclature_groups
        self.assertIn("Сырье", [g.name for g in groups.values()])

    def test_nomenclatures_created(self):
        """Должны создаться номенклатуры (Хлеб, Масло, Сыр)"""
        noms = self.service.nomenclatures
        names = [n.name for n in noms]
        for expected in ["Хлеб", "Масло сливочное", "Сыр"]:
            self.assertIn(expected, names)

    def test_recipes_created(self):
        """Проверяем наличие рецепта бутерброда"""
        recipes = self.service.recipes
        self.assertEqual(len(recipes), 1)
        recipe = recipes[0]
        self.assertIsInstance(recipe, recipe_model)
        self.assertEqual(recipe.name, "Бутерброд с маслом и сыром")

    def test_unique_elements_in_repository(self):
        """Все объекты внутри репозитория должны быть уникальны"""
        # Проверим уникальность единиц измерения
        measure_names = [mu.name for mu in self.service.measure_units.values()]
        self.assertEqual(len(measure_names), len(set(measure_names)),
                         "Дублирование в MeasureUnitModel")

        # Проверим уникальность групп
        group_names = [g.name for g in self.service.nomenclature_groups.values()]
        self.assertEqual(len(group_names), len(set(group_names)),
                         "Дублирование в NomenclatureGroupModel")

        # Проверим уникальность номенклатур
        nomenclature_names = [n.name for n in self.service.nomenclatures]
        self.assertEqual(len(nomenclature_names), len(set(nomenclature_names)),
                         "Дублирование в NomenclatureModel")

    def test_get_nomenclature_by_name(self):
        """Проверяем получение номенклатуры по имени"""
        nom = self.service.get_nomenclature("Сыр")
        self.assertIsNotNone(nom)
        self.assertIsInstance(nom, nomenclature_model)
        self.assertEqual(nom.name, "Сыр")


if __name__ == "__main__":
    unittest.main()
