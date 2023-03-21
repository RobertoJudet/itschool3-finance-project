from domain.user.user import User
import re


class InvalidUsername(Exception):
    pass


class UsernameNotValid(Exception):
    def __init__(self, username: str):
        super().__init__(
            f"Username '{username}' is not valid. Needs to be between 6 and 20 chars!"
        )


class UsernameNotCorrect(Exception):
    def __init__(self, username: str):
        super().__init__(
            f"Username '{username}' is not valid. It contains unwanted characters!"
        )


class UserFactory:
    @classmethod
    def create(cls, username: str) -> User:
        cls.validate_username(username)
        return User(username)

    @classmethod
    def validate_username(cls, username: str):
        if not 6 < len(username) < 20:
            raise UsernameNotValid(username)
        if not re.match("^[A-Za-z0-9_-]*$", username):
            raise UsernameNotCorrect(username)

    def make(self, username: str):
        if len(username) < 6:
            raise InvalidUsername
        return User(username)
