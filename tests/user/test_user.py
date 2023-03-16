import unittest

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

    @unittest.skip("TODO homework")
    def test_it_sets_empty_list_if_we_do_not_specify_stock(self):


    @unittest.skip("Homework")
    def test_it_sets_the_stock_we_give(self):
        # set  a list of 3 strings


if __name__ == '__main__':
    unittest.main()
