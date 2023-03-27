import uuid


class User:
    def __init__(self, username: str, stocks: list[str] = None, id: int = uuid.uuid4()):
        self.__username = username
        self.__stocks = stocks if stocks else []
        self.__id = id

    @property
    def username(self):
        return self.__username

    @property
    def stocks(self) -> list[str]:
        return self.__stocks


