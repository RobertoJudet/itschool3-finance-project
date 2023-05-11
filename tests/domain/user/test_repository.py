import os
import unittest

from pandas.conftest import cls

from domain.user.factory import UserFactory
from domain.user.repo import UserRepo
from persistence.user_file import UserPersistenceFile


def tearDownClass(cls) -> None:
    os.remove("test_users.json")


class UserRepositoryTestCase(unittest.TestCase):
    users_file = None

    def test_it_adds_a_user(self):
        expected_username = "a-username"
        new_user = UserFactory().make_new(expected_username)

        self.repo.add(new_user)

        actual_users = self.repo.get_all()

        self.assertEqual(expected_username, actual_users[1].username)

    @classmethod
    def setUpClass(cls) -> None:
        cls.users_file = "test_users.json"
        cls.repo = UserPersistenceFile(cls.users_file)

    def test_it_reads_a_user_from_the_system(self):
        repo = UserRepo(self.users_file)

        actual_users = self.repo.get_all()

        self.assertEqual(repo, len(actual_users))




if __name__ == "__main__":
    unittest.main()
