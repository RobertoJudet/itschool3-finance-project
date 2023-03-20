from fastapi import APIRouter

users_router = APIRouter(prefix="/users")


@users_router.get("/")
def get_all_users():
    return []


@users_router.delete("/")
def delete_user():
    pass


@users_router.post("/")
def create_a_user(username):
    pass
