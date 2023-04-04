# from domain.user.user import User
# import re
#
#
# class InvalidUsername(Exception):
#     pass
#
#
# class UsernameNotValid(Exception):
#     def __init__(self, username: str):
#         super().__init__(
#             f"Username '{username}' is not valid. Needs to be between 6 and 20 chars!"
#         )
#
#
# class UsernameNotCorrect(Exception):
#     def __init__(self, username: str):
#         super().__init__(
#             f"Username '{username}' is not valid. It contains unwanted characters!"
#         )
#
#
# class UserFactory:
#     @classmethod
#     def create(cls, username: str) -> User:
#         cls.validate_username(username)
#         return User(username)
#
#     @classmethod
#     def validate_username(cls, username: str):
#         if not 6 < len(username) < 20:
#             raise UsernameNotValid(username)
#         if not re.match("^[A-Za-z0-9_-]*$", username):
#             raise UsernameNotCorrect(username)
#
#     def make(self, username: str):
#         if len(username) < 6:
#             raise InvalidUsername
#         return User(username)

from domain.user.user import User
import uuid
import re


class InvalidUsername(Exception):
    pass


class UserNameNotCorrect(Exception):
    pass


class UserFactory:
    def make_new(self, username: str) -> User:
        if 20 < len(username) < 6:
            raise InvalidUsername
        if not re.match("^[A-Za-z0-9_-]*$", username):
            raise UserNameNotCorrect(username)
        user_uuid = uuid.uuid4()
        return User(user_uuid, username)

    def make_from_persistance(self, info: tuple) -> User:
        return User(
            uuid=uuid.UUID(info[0]),
            username=info[1],
            stocks=info[2],
        )
