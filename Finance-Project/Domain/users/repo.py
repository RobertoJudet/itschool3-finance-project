import json

from Domain.users.factory import UserFactory
from Domain.users.persistance_interface import UserPersistenceInterface
from Domain.users.user import User


class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        self.__persistence = persistence
        self.__users = None
# Todo refactor to not have duplicate code

    def add(self, new_user: User):
        if self.__users is None:
            self.__users = self.__persistence.get_all()
        self.__users.append(new_user)
        self.__persistence.add(new_user)

    def get_all(self) -> list[User]:
        if self.__users is []:
            self.__users = self.__persistence.get_all()
        return self.__users

    def get_by_username(self, username: str) -> User:
        for u in self.__users:
            if u.username == username:
                return u


    def write_to_file(self):
        users_info = [(str(x.id), x.username, x.stocks) for x in self.__users]
        users_json = json.dumps(users_info)
        with open(self.file_path, "w") as file:
            file.write(users_json)



