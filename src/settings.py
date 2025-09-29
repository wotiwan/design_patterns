from src.models.company_model import company_model
from src.core.validator import validator

class settings:
    __company = None

    def __init__(self):
        self.__company = company_model()

    # Геттер __company
    @property
    def company(self) -> company_model:
        return self.__company

    def set_inn(self, value:int):
        validator.validate(value, int, 12, True)
        self.__company.inn = value

    def set_account(self, value:int):
        validator.validate(value, int, 11, True)
        self.__company.account = value

    def set_correspondent_account(self, value:int):
        validator.validate(value, int, 11, True)
        self.__company.correspondent_account = value

    def set_bik(self, value:int):
        validator.validate(value, int, 9, True)
        self.__company.bik = value

    def set_ownership_type(self, value:str):
        validator.validate(value, str, 5, True)
        self.__company.ownership_type = value.strip()
