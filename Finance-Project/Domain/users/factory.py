import uuid
from Domain.users.user import User


class InvalidUsername(Exception):
    pass


class UserFactory:
    # username should be at least 6 chars and max 20 chars, it can only contain letter, number & -
    def make_new(self, username: str) -> User:
        if len(username) < 6 or len(username) > 20:
            raise InvalidUsername("Username should have between 6 and 20 characters")
        if not all(c.isalnum() or c == "-" for c in username):
            raise InvalidUsername("Username should only contain letters, numbers, and hyphens")
        user_uuid = uuid.uuid4()
        return User(user_uuid, username)

    def make_from_persistance(self, info: tuple) -> User:
        return User(
            uuid=uuid.UUID(info[0]),
            username=info[1],
            stocks=info[2],
        )
