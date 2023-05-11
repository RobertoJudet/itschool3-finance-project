from fastapi import APIRouter, Depends

from Domain.Asset.factory import AssetFactory
from Domain.Asset.repo import AssetRepo
from Domain.users.repo import UserRepo
from Domain.users.factory import UserFactory
from API.models import UserAdd, UserInfo, AssetInfoUser, AssetAdd
from Persistence.user_file import UserPersistenceFile
from Persistence.user_sqlite import UserPersistenceSqlite

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


@users_router.post("", response_model=UserInfo)
def create_a_user(new_user: UserAdd, repo=Depends(get_user_repo)):
    user = UserFactory().make_new(new_user.username)
    repo.add(user)
    return user

@users_router.post("/{user_id}/assets", response_model=AssetInfoUser)
def add_asset_to_user(user_id: str, asset: AssetAdd, repo=Depends(get_user_repo)):
    new_asset = AssetFactory().make_new(asset.ticker)
    user = repo.get_by_id(user_id)
    AssetRepo().add_to_user(user, new_asset)
    return new_asset