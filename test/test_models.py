from src.models.company_model import company_model
from src.settings_manager import settings_manager
import json
import unittest

class TestModels(unittest.TestCase):

    # Проверка создания основной модели
    # Данные после создания должны быть пустыми
    def test_empty_company_model(self):
        # Подготовка
        model = company_model()

        # Действие

        #Тест
        self.assertEqual(model.name, "")

    # Проверка создания основной модели
    # Данные меняем. Данные должны быть
    def test_notEmpty_company_model(self):
        # Подготовка
        model = company_model()

        # Действие
        model.name = "test"

        # Тест
        self.assertNotEqual(model.name, "")

    # Проверка загрузки названия из конфига
    def test_load_createmodel_companymodel(self):
        # Подготовка
        file_name = "D:/учёба/Volovikov/design_patterns/settings.json"
        manager1 = settings_manager(file_name)
        manager2 = settings_manager(file_name)

        # Действие
        manager1.load()
        # manager2.load() Больше не нужно, т.к. manager1 и manager2 - один и тот же экземпляр класса

        # Проверки
        self.assertEqual(manager1.settings, manager2.settings)

    # Проверка загрузки всех свойств в объект от класса settings
    # (инкапсулированный от settings_manager)
    def test_load_settings(self):
        # Подготовка
        file_name = "D:/учёба/Volovikov/design_patterns/settings.json"
        manager = settings_manager(file_name)

        # Действие
        manager.load()

        # Тесты
        self.assertEqual(manager.settings.company.inn, 380113335012)
        self.assertEqual(manager.settings.company.account, 12345678901)
        self.assertEqual(manager.settings.company.correspondent_account, 12345678901)
        self.assertEqual(manager.settings.company.bik, 123456789)
        self.assertEqual(manager.settings.company.ownership_type, "OOOAO")

    def test_different_config_locations(self):
        # Подготовка
        file_name = "../settings.json"
        file_name2 = "../cfg/settings2.json"
        manager = settings_manager(file_name)

        # Действие №1
        manager.load()

        # Проверка №1
        self.assertEqual(manager.settings.company.name, "Рога и копыта")

        # Действие №2
        manager.file_name = file_name2
        manager.load()

        # Проверка №2. Убеждаемся что с другого файла были загружены настройки
        self.assertEqual(manager.settings.company.name, "Теремок")

    # Проверка негативного сценария обновления атрибутов организации
    def test_wrong_config_data(self):
        file_name = "../settings.json"
        manager = settings_manager(file_name)

        # Действие
        manager.load()

        # Проверка. Неверно указан инн
        self.assertRaises(ValueError, manager.settings.set_inn, 123)
        # Неверно указан счёт
        self.assertRaises(ValueError, manager.settings.set_account, 123)
        # Неверно указан корреспондентский счёт
        self.assertRaises(ValueError, manager.settings.set_correspondent_account, 123)
        # Неверно указан БИК
        self.assertRaises(ValueError, manager.settings.set_bik, 123)


if __name__ == "__main__":
    unittest.main()
