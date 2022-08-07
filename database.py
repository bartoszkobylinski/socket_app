
from __future__ import with_statement
import json
from turtle import width


def create_databse():
    with open('database.json', "w") as db:
        print("Database has been created")
        db.write(json.dumps({'users':[]}))

def check_if_user_exists_in_database(username):
    with open ('database.json', 'r') as db:
        json_database = json.load(db)
    for usersname in json_database.get("users",''):
        if username in usersname.get("user",''):
            return True
        else:
            return False

def check_queryset_in_the_database(**kwargs):
    with open ('database.json', 'r') as db:
        json_database = json.load(db)

    for user in json_database.get('users',''):
        if kwargs in user.get('user',''):
            return True
        else:
            return False


def add_user_to_database(user, password):
    with open ('database.json', 'r') as db:
        json_database = json.load(db)
    if len(json_database.get('users','')) < 1:
        json_database['users'].append({'user': user, 'password':password, "mailbox": list(), 'admin': True})
    else:
        json_database['users'].append({'user': user, 'password':password, 'mailbox': list(), 'admin': False})
    
    with open("database.json", "w") as db:
        json.dump(json_database, db)        
        
def remove_from_database(data):
    with open('database', 'w') as db: 

        pass

def update_record_in_databe(data):
    with open('database', 'w') as db:
        pass

def authorize_user(username, password):
    with open ('database.json','r') as db:
        json_database = json.load(db)

    for user in json_database.get('users',''):
        if username == user.get('user','') and password == user.get('password',''):
            return True
        else:
            return False
def add_message_to_user_mailbox(username, message):
    with open('database.json','r') as db:
        json_database = json.load(db)

    for user in json_database.get("users",''):
        if username == user.get("user",''):
            if len(user.get("mailbox",''))< 5:
                user.get("mailbox",'').append(message)
                with open("database.json", "w") as db:
                    json.dump(json_database, db) 
                return True
            else:
                return False
{
    'users': [
        {'name':'bartek','email':'kal@wp.pl','password':'jOKotas324',
        'admin':True, 'logged':False, "messages":['oeuoe','oeuoeu','oeuoeu']}
    ]
}
