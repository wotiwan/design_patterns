import time

from src.models.company_model import company_model
from src.models.storage_model import storage_model
from src.models.nomenclature_model import nomenclature_model
from src.models.nomenclature_group_model import nomenclature_group_model
from src.models.range_model import range_model

from src.core.validator import argument_exception, operation_exception

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
        self.assertRaises(argument_exception, manager.settings.set_inn, 123)
        # Неверно указан счёт
        self.assertRaises(argument_exception, manager.settings.set_account, 123)
        # Неверно указан корреспондентский счёт
        self.assertRaises(argument_exception, manager.settings.set_correspondent_account, 123)
        # Неверно указан БИК
        self.assertRaises(argument_exception, manager.settings.set_bik, 123)

    # Проверка на сравнение двух по значению одинаковых моделей
    def test_equals_storage_model_create(self):
        # Подготовка
        storage1 = storage_model()
        storage2 = storage_model()

        # Действие
        storage2.unique_code = storage1.unique_code

        # Проверки
        self.assertEqual(storage1, storage2)

    def test_range_model_create(self):
        # Подготовка
        gramms = range_model("Гр.", 1)
        kilos = range_model("Кг.", 1000, gramms)

        # Действие

        # Проверка
        self.assertEqual(gramms.name, "Гр.")
        self.assertEqual(kilos.name, "Кг.")
        self.assertEqual(gramms.base_range, None)
        self.assertEqual(kilos.base_range, gramms)
        self.assertEqual(gramms.conversation_ratio, 1)
        self.assertEqual(kilos.conversation_ratio, 1000)

    def test_correct_data_range_model(self):
        # Подготовка
        gramms = range_model("Гр.", 1)

        # Действие
        gramms.base_range = gramms
        gramms.conversation_ratio = 1000

        # Проверка
        self.assertEqual(gramms.base_range, gramms)
        self.assertEqual(gramms.conversation_ratio, 1000)

    def test_wrong_data_range_model(self):
        # Подготовка
        gramms = range_model("Гр.", 1)

        # Действие

        # Проверка
        with self.assertRaises(argument_exception):
            gramms.base_range = "some string" # Неверный тип данных

        with self.assertRaises(argument_exception):
            gramms.conversation_ratio = "some string" # Неверный тип данных

    def test_nomenclature_model_create(self):
        # Подготовка
        nomenclature = nomenclature_model()

        # Действие
        nomenclature.full_name = "Перфоратор"

        # Проверка
        self.assertEqual(nomenclature.full_name, "Перфоратор")

    def test_wrong_data_nomenclature_model(self):
        # Подготовка
        nomenclature = nomenclature_model()

        # Действие
        with self.assertRaises(argument_exception):
            nomenclature.full_name = "1" * 256 # Длина выше допустимой
        with self.assertRaises(argument_exception):
            nomenclature.full_name = 1 # Неправильный тип

if __name__ == "__main__":
    unittest.main()
