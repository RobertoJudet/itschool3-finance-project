# from fastapi import APIRouter
# from api.models import UserAdd, UserInfo
# from domain.user.factory import UserFactory
# from domain.user.repository import UserRepo
#
#
# users_router = APIRouter(prefix="/users")
# repo = UserRepository()
#
#
# @users_router.get("", response_model=list[UserInfo])
# def get_all_users():
#     users = repo.get_all()
#     with open("usernames.txt", "w") as f:
#         for user in users:
#             f.write(user.username + "\n")
#     return [UserInfo(name=u.username, stocks=u.stocks) for u in users]
#
#
# @users_router.delete("/")
# def delete_user(username: str):
#     repo.delete(username)
#
#
# @users_router.post("", response_model=UserInfo)
# def create_a_user(user: UserAdd):
#     new_user = UserFactory.create(user.name)
#     repo.add(new_user)
#     return UserInfo(name=new_user.username, stocks=new_user.stocks)

# Homework 1 for Project
# implement get, create and delete user in domain too (user repo & user factory)
# also create api models
# create tests for repo & factory
# username should be at least 6 chars and max 20 chars, it can only contain letter, numbers & -
# save the user list in a file

from fastapi import APIRouter

from domain.user.repo import UserRepo
from domain.user.factory import UserFactory
from api.models import UserAdd, UserInfo

users_router = APIRouter(prefix="/users")

repo = UserRepo("main_user.json")
# Homework 1 for Project
# implement get, create and delete user in domain too (user repo & user factory)
# also create api models
# create tests for repo & factory
# username should be at least 6 chars and max 20 chars, it can only contain letter, numbers & -
# save the user list in a file


@users_router.get("", response_model=list[UserInfo])
def get_all_users():
    return repo.get_all()


@users_router.get("/{username}", response_model=UserInfo)
def get_user(username: str):
    return repo.get_by_username(username)


@users_router.post("")
def create_a_user(new_user: UserAdd):
    user = UserFactory().make(new_user.username)
    repo.add(user)
