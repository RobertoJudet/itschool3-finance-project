import json

from domain.user.user import User


class UserRepo:
    def __init__(self, file_path: str):
        self.file_path = file_path
        try:
            file = open(file_path)
            contents = file.read()
            file.close()
            users_info = json.loads(contents)
            self.__users = [User(x) for x in users_info]
        except:
            self.__users = []

    def add(self, new_user: User):
        self.__users.append(new_user)
        users_info = [x.username for x in self.__users]
        # TODO homework refactor with
        users_json = json.dumps(users_info)
        file = open(self.file_path, "w")
        file.write(users_json)
        file.close()

    def get_all(self) -> list[User]:
        return self.__users

    def get_by_username(self, username: str) -> User:
        for u in self.__users:
            if u.username == username:
                return u
