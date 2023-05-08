import unittest
import uuid

from domain.asset.asset import Asset
from domain.user.user import User


class UserMyTestCase(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        # set up
        username = "random-generated"
        id_ = uuid.uuid4()
        user = User(id_, username)
        # execution
        actual_username = user.username
        # assertion
        self.assertEqual(username, actual_username)

    @unittest.skip("TODO: HOMEWORK")
    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):
        user = User("random-username")

        actual_stocks = user.stocks

        self.assertEqual([], actual_stocks)

    @unittest.skip("TODO: homework")
    def test_it_sets_the_stocks_we_give(self):
        id_ = uuid.uuid4()
        username = "nume-random"

        actual_asset = [
            Asset(country="romania", ticker="aapl", nr=0, name="Apple", sector="Tech")
        ]

        user = User(id_, username, actual_asset)

        actual = user.stocks

        self.assertEqual(actual_asset, actual)


if __name__ == "__main__":
    unittest.main()
