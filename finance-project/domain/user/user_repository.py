from domain.user.user import User


class UserRepository:
    def __init__(self):
        self.__users = []

    def add(self, username: User):
        self.__users.append(username)

    def get_all(self) -> list[User]:
        return self.__users

    def delete(self, username: str):
        self.__users = [u for u in self.__users if u.username != username]
