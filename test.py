
import json
import unittest

from user import User
from database import check_if_user_exists_in_database, create_databse, add_user_to_database, read_all_user_mailbox, read_user_mailbox
import os


# User file

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(name='bartek', password='halina')

    def test_initial_value_of_user_class(self):
        self.assertIsInstance(self.user, User)
    
    def test_string_method(self):
        self.assertEqual(str(self.user), 'bartek logged: False admin: False')


# database file

class TestDatabase(unittest.TestCase):
    
    def test_if_database_is_created(self):
        create_databse("test_database.json")
        path_to_database = '/Users/bartoszkobylinski/Programming/Python/socket_server/test_database.json'
        self.assertTrue(os.path.exists(path_to_database))

    def test_if_user_is_added_to_database(self):
        user = 'bartek'
        password = 'halina'
        add_user_to_database(user=user, password=password)
        self.assertEqual(check_if_user_exists_in_database(username=user), True)
     
    def test_if_user_exists_in_database(self):
        self.assertEqual(True, check_if_user_exists_in_database(username = 'bartek'))
    
    def test_read_user_mailbox(self):
    
        with open ('test_database.json','r') as db:
            test_json_database = json.load(db)
            read_mailbox = 1
            for user in test_json_database.get('users',''):
                if user.get('user','') == 'bartek':
                    user.get("unread_mailbox").append("halina, hahlina")      
            with open('test_database.json','w') as db:
                json.dump(test_json_database, db)
        read_user_mailbox('bartek')
        with open('test_database.json', 'r') as db:
            test_json_database = json.load(db)
            self.assertEqual(1, len(test_json_database['users'][0]['mailbox']))
    
    def test_read_all_user_mailbox(self):
        mails = read_all_user_mailbox()
        print(f"to jest mails: {mails}")
        mails_quantity = 0 
        for user in mails:
            mails_quantity += int(len(user.get("unread_mailbox",'')))
            print(f"mail_quantity: {mails_quantity}")

        self.assertEqual(4, mails_quantity)

 
if __name__ == '__main__':
    unittest.main()
