import unittest

from domain.user.user import User


class UserMyTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        username = "random_generated"
        user = User(username)
        actual_username = user.username
        self.assertEqual(username, actual_username)

    @unittest.skip("TODO: HOMEWORK")
    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):
        user = User("random-username")

        actual_stocks = user.stocks

        self.assertEqual([], actual_stocks)

    @unittest.skip("TODO: homework")
    def test_it_sets_the_stocks_we_give(self):
        pass


if __name__ == "__main__":
    unittest.main()
