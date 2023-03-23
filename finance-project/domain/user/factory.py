from domain.user.user import User

class InvalidUsername(Exception):
    pass
class UserFactory:
    def make(self, username: str) -> User:
        if len(username) < 6:
            raise InvalidUsername
        return User(username)

