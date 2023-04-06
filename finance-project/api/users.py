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

from domain.asset.factory import AssetFactory
from domain.asset.repo import AssetRepo
from domain.user.repo import UserRepo
from domain.user.factory import UserFactory
from api.models import UserAdd, UserInfo, AssetInfoUser, AssetAdd
from persistence.user_file import UserPersistenceFile
from persistence.user_sqlite import UserPersistenceSqlite

users_router = APIRouter(prefix="/users")

# user_persistence = UserPersistenceFile("main_user.json")
user_persistence = UserPersistenceSqlite()
repo = UserRepo(user_persistence)


# Homework 1 for Project
# implement get, create and delete user in domain too (user repo & user factory)
# also create api models
# create tests for repo & factory
# username should be at least 6 chars and max 20 chars, it can only contain letter, numbers & -
# save the user list in a file

# TODO GET /users/{user_id}


@users_router.get("", response_model=list[UserInfo])
def get_all_users():
    return repo.get_all()


@users_router.get("/{user_id}", response_model=UserInfo)
def get_user(user_id: str):
    return repo.get_by_id(user_id)


@users_router.post("", response_model=UserInfo)
def create_a_user(new_user: UserAdd):
    user = UserFactory().make_new(new_user.username)
    repo.add(user)
    return user


# TODO delete a user, DELETE /users/{user_id}


# TODO fix api return asset info
@users_router.post("/{user_id}/asset", response_model=AssetInfoUser)
def add_asset_to_user(user_id: str, asset: AssetAdd):
    new_asset = AssetFactory().make_new(asset.ticker)
    user = repo.get_by_id(user_id)
    # user.add_stock(new_asset)
    AssetRepo().add_to_user(user, new_asset)
    return new_asset
