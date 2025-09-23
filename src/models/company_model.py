
class company_model:
    __name:str = ""                   # Наименование компании
    __inn:str = ""                    # ИНН
    __account:str = ""                # Счёт
    __correspondent_account:str = ""  # Корреспондентский счёт
    __bik:str = ""                    # БИК
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
    def inn(self) -> str:
        return self.__inn

    @inn.setter
    def inn(self, value:str):
        if value.strip() != "":
            self.__inn = value.strip()


    # account setter and getter
    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value:str):
        if value.strip() != "":
            self.__account = value.strip()


    # correspondent_account setter and getter
    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if value.strip() != "":
            self.__correspondent_account = value.strip()


    # bik setter and getter
    @property
    def bik(self):
        return self.__bik

    @bik.setter
    def bik(self, value:str):
        if value.strip() != "":
            self.__bik = value.strip()


    # ownership_type setter and getter
    @property
    def ownership_type(self):
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value:str):
        if value.strip() != "":
            self.__ownership_type = value.strip()