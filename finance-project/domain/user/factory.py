from domain.user.user import User

class InvalidUsername(Exception):
    pass

class UserFactory:

    def make(self, username: str) -> User:
        for i in username:
            if not (i.isalnum() or i == "-"):
                raise InvalidUsername("User is not valid")
            else:
                raise InvalidUsername("User is valid")
        if len(username) < 6 or len(username) > 20:
            raise InvalidUsername("Username should have at least 6 characters or maximum 20 characters")
        else:
            return User(username)


