import uuid

from fastapi import APIRouter

from Domain.Asset.factory import AssetFactory
from Domain.users.factory import UserFactory
from Domain.users.repo import UserRepo
from API.models import UserAdd, UserInfo, AssetInfoUser

users_router = APIRouter(prefix="/users")

repo = UserRepo("main_users.json")


@users_router.get("", response_model=list[UserInfo])
def get_all_users():
    return repo.get_all()


# when we query a single user or delete a user we should pass the id


@users_router.get("/users{user_id}", response_model=UserInfo)
def get_user(username: str):
    return repo.get_by_username(username)


@users_router.post("", response_model=UserInfo)
def create_a_user(new_user: UserAdd):
    user = UserFactory().make_new(new_user.username)
    repo.add(user)
    return user


# TODO delete a user, DELETE /users/{user_id}

@users_router.post("/{user_id}/assets", response_model=AssetInfoUser)
def add_asset_to_user(user_id: str, ticker: str):
    asset = AssetFactory().make_new(ticker)
    print(asset.__dict__)
    return asset
