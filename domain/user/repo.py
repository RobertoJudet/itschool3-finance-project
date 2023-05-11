import json
import uuid

from domain.asset.repo import AssetRepo
from domain.user.persistence_interface import UserPersistenceInterface
from domain.user.user import User
from singleton import singleton


@singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        print("Initializing user repo")
        self.__persistence = persistence
        self.__users = None

    def add(self, new_user: User):
        self.__check_we_have_users()
        self.__persistence.add(new_user)
        self.__users.append(new_user)

    def get_all(self) -> list[User]:
        self.__check_we_have_users()
        return self.__users

    def get_by_id(self, uid: str) -> User:
        self.__check_we_have_users()
        for u in self.__users:
            if u.id == uuid.UUID(hex=uid):
                assets = AssetRepo().get_for_user(u)
                return User(
                    uuid=u.id,
                    username=u.username,
                    stocks=assets
                )

    def delete_by_id(self, user_id: User.id):
        self.__check_we_have_users()
        self.__persistence.delete_by_id(user_id)
        for u in self.__users:
            if user_id == u.id:
                self.__users.remove(u)
        self.__users = None
        self.__check_we_have_users()

    def edit_by_id(self, user_id: User.id, username: str):
        self.__check_we_have_users()
        for u in self.__users:
            if user_id == u.id:
                u.username = username
        self.__persistence.edit_by_id(user_id, username)
        self.__users = None
        self.__check_we_have_users()

    def __check_we_have_users(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()
