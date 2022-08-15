
import unittest

from user import User

class TestUser(unittest.TestCase):

    def test_initial_value_of_user_class(self):
        user = User(name='bartek', password='halina')
        self.assertIsInstance(user, User)
    
    def test_string_method(self):
        user = User(name='bartek', password='tomek')
        self.assertEqual(str(user), 'bartek logged: False admin: False')



if __name__ == '__main__':
    unittest.main()
