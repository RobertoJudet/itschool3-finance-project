import uuid
from domain.user.user import User


class InvalidUsername(Exception):
    pass


class UserFactory:
    def make_new(self, username: str) -> User:
        for i in username:
            if not (i.isalnum() or i == "-"):
                raise InvalidUsername("User is not valid")
        if len(username) < 6 or len(username) > 20:
            raise InvalidUsername(
                "Username should have at least 6 characters or maximum 20 characters"
            )
        else:
            user_uuid = uuid.uuid4()
            return User(user_uuid, username)

    def make_from_persistence(self, info: tuple) -> User:
        return User(
            uuid=uuid.UUID(info[0]),
            username=info[1],
        )
