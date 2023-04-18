from fastapi import APIRouter, Depends

from api.models import UserAdd, UserInfo, AssetInfoUser, AssetAdd
from domain.asset.factory import AssetFactory
from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.repo import UserRepo
from persistence.user_sqlite import UserPersistenceSqlite
from persistence.user_file import UserPersistenceFile

users_router = APIRouter(prefix="/users")


def get_user_repo() -> UserRepo:
    # user_persistence = UserPersistenceFile("main_users.json")
    user_persistence = UserPersistenceSqlite()
    return UserRepo(user_persistence)


@users_router.get("", response_model=list[UserInfo])
def get_all_users(repo=Depends(get_user_repo)):
    return repo.get_all()


@users_router.get("/{user_id}", response_model=UserInfo)
def get_user(user_id: str, repo=Depends(get_user_repo)):
    return repo.get_by_id(user_id)


def add_asset_to_user(user_id: str, asset: AssetAdd):
    new_asset = AssetFactory().make_new(asset.ticker)
    user = repo.get_by_id(user_id)
    # user.add_stock(new_asset)
    AssetRepo().add_to_user(user, new_asset)
    return new_asset


@users_router.post("", response_model=UserInfo)
def create_a_user(new_user: UserAdd, repo=Depends(get_user_repo)):
    user = UserFactory().make_new(new_user.username)
    repo.add(user)
    return user


@users_router.delete("")
def delete_by_username(username: str):
    pass


@users_router.post("/{user_id}/assets", response_model=AssetInfoUser)
def add_asset_to_user(user_id: str, asset: AssetAdd, repo=Depends(get_user_repo)):
    new_asset = AssetFactory().make_new(asset.ticker)
    user = repo.get_by_id(user_id)
    AssetRepo().add_to_user(user, new_asset)
    return new_asset
