import json
from abc import ABC

from Domain.users.factory import UserFactory
from Domain.users.persistance_interface import UserPersistenceInterface
from Domain.users.user import User


class UserPersistenceFile(UserPersistenceInterface, ABC):
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all_users(self) -> list[User]:
        try:
            with open(self.__file_path) as file:
                contents = file.load()
                users_info = json.loads(contents)
            factory = UserFactory()
            return [factory.make_from_persistence(x) for x in users_info]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_user(self, user: User):
        current_users = self.get_all_users()
        current_users.append(user)
        users_dict = [u.to_dict() for u in self.__users]
        users_dict.append(user.to_dict())

        
        with open(self.__file_path, "w") as f:
            json.dump(users_dict, f)
