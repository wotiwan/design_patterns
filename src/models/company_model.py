
class company_model:
    __name:str = ""                   # Наименование компании
    __inn:int = ""                    # ИНН
    __account:int= ""                # Счёт
    __correspondent_account:int = ""  # Корреспондентский счёт
    __bik:int = ""                    # БИК
    __ownership_type:str = ""         # Форма собственности


    # name setter and getter
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value:str):
        if value.strip() != "":
            self.__name = value.strip()


    # inn setter ang getter
    @property
    def inn(self) -> int:
        return self.__inn

    @inn.setter
    def inn(self, value:int):
        if value is not None:
            self.__inn = value


    # account setter and getter
    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value:int):
        if value is not None:
            self.__account = value


    # correspondent_account setter and getter
    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: int):
        if value is not None:
            self.__correspondent_account = value


    # bik setter and getter
    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value:int):
        if value is not None:
            self.__bik = value


    # ownership_type setter and getter
    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value:str):
        if value.strip() != "":
            self.__ownership_type = value.strip()