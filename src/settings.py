from rOMASHKA.src.models.company_model import company_model

class settings:
    __company = None

    def __init__(self):
        self.__company = company_model()

    # Геттер __company
    @property
    def company(self) -> company_model:
        return self.__company

    def set_inn(self, value:str):
        self.__company.inn = self.__validate_str(value, 12, "ИНН")

    def set_account(self, value:str):
        self.__company.account = self.__validate_str(value, 11, "Счет")

    def set_correspondent_account(self, value:str):
        self.__company.correspondent_account = self.__validate_str(
            value, 11, "Корреспондентский счёт")

    def set_bik(self, value:str):
        self.__company.bik = self.__validate_str(value, 9, "БИК")

    def set_ownership_type(self, value:str):
        self.__company.ownership_type =  self.__validate_str(
            value, 5, "Вид собственности")

    def __validate_str(self, value: str, length: int, field: str) -> str:
        value = value.strip()
        if len(value) != length:
            raise ValueError(f"{field} должен содержать ровно {length} символов")
        return value