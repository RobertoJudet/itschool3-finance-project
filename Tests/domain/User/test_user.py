import unittest
from Domain.users.user import User


class UserMyTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        # setup
        username = "random_generated"
        user = User(username)
        # execute
        actual_username = user.username
        # assertion
        self.assertEqual(username, actual_username)

    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):
        user = User("random-username")

        actual_stocks = user.stocks

        self.assertEqual([], actual_stocks)

    @unittest.skip("TODO: homework")
    def test_it_sets_the_stocks_we_give(self):
        # set a list of 3 string
        pass


# De revazut filmarea de joi
