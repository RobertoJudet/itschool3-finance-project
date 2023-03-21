from fastapi import APIRouter
from api.models import UserAdd, UserInfo
from domain.user.user_factory import UserFactory
from domain.user.user_repository import UserRepository


users_router = APIRouter(prefix="/users")
repo = UserRepository()


@users_router.get("", response_model=list[UserInfo])
def get_all_users():
    users = repo.get_all()
    with open("usernames.txt", "w") as f:
        for user in users:
            f.write(user.username + "\n")
    return [UserInfo(name=u.username, stocks=u.stocks) for u in users]


@users_router.delete("/")
def delete_user(username: str):
    repo.delete(username)


@users_router.post("", response_model=UserInfo)
def create_a_user(user: UserAdd):
    new_user = UserFactory.create(user.name)
    repo.add(new_user)
    return UserInfo(name=new_user.username, stocks=new_user.stocks)
