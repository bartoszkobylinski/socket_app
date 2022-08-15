
import unittest

from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(name='bartek', password='halina')

    def test_initial_value_of_user_class(self):
        self.assertIsInstance(self.user, User)
    
    def test_string_method(self):
        self.assertEqual(str(self.user), 'bartek logged: False admin: False')



if __name__ == '__main__':
    unittest.main()
