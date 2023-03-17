import unittest

from domain.user import user
from domain.user.user import User


class UserTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        #set up
        username = "random generate"
        user = User(username)
        # execution
        actual_username = user.username

        #assertion
        self.assertEqual(username, actual_username)


    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):
        # set up
        stocks = []
        stock = User(stocks)
        # execution
        actual_stock = stock.stocks
        # assertion
        self.assertEqual(stocks, actual_stock)


    def test_it_sets_the_stock_we_give(self):
        # set  a list of 3 strings
        # set up
        stocks = ["user1", "user2", "user3"]
        stock = User(stocks)
        # execution
        actual_stock = stock.stocks
        # assertion
        self.assertNotEqual(stocks, actual_stock)


if __name__ == '__main__':
    unittest.main()
