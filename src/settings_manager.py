import os.path
from src.settings import settings
import json

class settings_manager:
    __file_name:str = ""
    __settings:settings = None

    # Чтобы не создавать класс каждый раз заново
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self, file_name:str):
        self.file_name = file_name
        self.default()

    # Отдаём настройки только для чтения (инкапсуляция)
    @property
    def settings(self) -> settings:
        return self.__settings

    @property
    def file_name(self):
        return self.__file_name

    # Возможность поменять путь до файла настроек
    @file_name.setter
    def file_name(self, value:str):
        if value.strip() == "":
            return
        if os.path.exists(value):
            self.__file_name = os.path.abspath(value.strip())

    def load(self) -> bool:
        if self.__file_name.strip() == "":
            raise FileNotFoundError
        try:
            file = open(self.__file_name, 'r', encoding='utf-8')
            data = json.load(file)
            self.convert(data)
            return True
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return False

    # Применение загруженных настроек
    def convert(self, data):
        try:
            # TODO: Сделать словарь ключей
            if "company" in data.keys():
                item = data["company"]
                self.__settings.company.name = item["name"]
                self.__settings.set_inn(item["inn"])
                self.__settings.set_bik(item["bik"])
                self.__settings.set_ownership_type(item["ownership_type"])
                self.__settings.set_account(item["account"])
                self.__settings.set_correspondent_account(item["correspondent_account"])
            else:
                raise Exception("Invalid config file!")
        except KeyError as e:
            raise KeyError(f"Отсутствует обязательное поле в 'company': {e}")
        except Exception as e:
            raise Exception(f"Ошибка при разборе раздела 'company': {e}")

    # Инициализируемые по умолчанию значения
    def default(self):
        self.__settings = settings()
        self.__settings.company.name = "Рога и копыта"
        self.__settings.set_inn(123456789012)
        self.__settings.set_bik(123456789)
        self.__settings.set_ownership_type("#####")
        self.__settings.set_account(12345678901)
        self.__settings.set_correspondent_account(12345678901)
