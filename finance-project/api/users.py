from fastapi import APIRouter, Depends
import json
from domain.asset.factory import AssetFactory
from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.repo import UserRepo
from api.models import UserAdd, UserInfo, AssetInfoUser, AssetAdd
from persistence.user_file import UserPersistenceFile
from persistence.user_sqlite import UserPersistenceSqlite
import logging

users_router = APIRouter(prefix="/users")


class InvalidPersistenceType(Exception):
    pass


def check_persistence_type(file_path):
    with open(file_path, "r") as config_info:
        persistence_type = config_info.read()
        data = json.loads(persistence_type)
        if "sqlite" in str(data["persistence"]):
            return UserPersistenceSqlite()
        elif "json" in str(data["persistence"]):
            return UserPersistenceFile("main_users.json")
        else:
            raise InvalidPersistenceType(
                "Unrecognized persistence config type. Please check config.json file."
            )


def get_user_repo() -> UserRepo:
    user_persistence = check_persistence_type("config.json")
    # user_persistence = UserPersistenceFile("main_users.json")
    # user_persistence = UserPersistenceSqlite()
    return UserRepo(user_persistence)


def get_asset_repo() -> AssetRepo:
    asset_persistence = set_asset_persistence_type("configuration/config.json")
    return AssetRepo(asset_persistence)


@users_router.get("", response_model=list[UserInfo])
def get_all_users(repo=Depends(get_user_repo)):
    return repo.get_all()


@users_router.get("/{user_id}", response_model=UserInfo)
def get_user_by_id(user_id: str, repo=Depends(get_user_repo)):
    return repo.get_by_id(user_id)


# @users_router.get("/{username}", response_model=UserInfo)
# def get_user(username: str):
# return repo.get_by_username(username)


@users_router.delete("/{user_id}")
def delete_user(user_id: str, repo=Depends(get_user_repo)):
    repo.delete_by_id(user_id)


@users_router.post("", response_model=UserInfo)
def create_a_user(new_user: UserAdd, repo=Depends(get_user_repo)):
    logging.info("Creating user...")
    user = UserFactory().make_new(new_user.username)
    try:
        repo.add(user)
        logging.info("Successfully created...")
    except Exception as e:
        logging.error("Could not create. Reason: " + str(e))
    repo.add(user)
    return user


@users_router.put("/{user_id}", response_model=UserInfo)
def edit_by_id(user_id: str, username: str, repo=Depends(get_user_repo)):
    repo.edit(user_id, username)
    return repo.get_by_id(user_id)


# TODO fix api, return asset info
@users_router.post("/{user_id}/assets", response_model=AssetInfoUser)
def add_asset_to_user(user_id: str, asset: AssetAdd, repo=Depends(get_user_repo)):
    new_asset = AssetFactory().make_new(asset.ticker)
    # TODO homework, if asset exception throw 400/404
    user = repo.get_by_id(user_id)
    # TODO homework, check we have a user otherwise throw exception code 404
    # user.add_stock(new_asset)
    print(user)
    AssetRepo().add_to_user(user, new_asset)

    return new_asset
