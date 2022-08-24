import json


def create_databse(name):
    with open(name, "w") as db:
        print("Database has been created")
        db.write(json.dumps({'users':[]}))

def check_if_user_exists_in_database(username):
    with open ('test_database.json', 'r') as db:
        json_database = json.load(db)
    for usersname in json_database.get("users",''):
        if username in usersname.get("user",''):
            return True
        else:
            return False
    
def read_user_mailbox(username):
    mailbox_to_show = list()
    with open('test_database.json','r') as db:
        json_database = json.load(db) 
        for user in json_database.get("users",''):
            if username == user.get("user",''):
                unread_mailbox = user.get("unread_mailbox")
                mailbox_to_show = unread_mailbox
                user.get("mailbox").extend(unread_mailbox)
                user["unread_mailbox"] = list()
        with open("test_database.json", 'w') as db:
            json.dump(json_database, db)  
    return mailbox_to_show

def read_all_user_mailbox():
    with open ('test_database.json','r') as db:
        all_unread_mailbox = list()
        json_database = json.load(db)
        print(f"to jest baza danych po zaladowaniu: {json_database}")
        for user in json_database.get("users",''):
            print(f"jestesmy na takim user: {user}")
            unread_mailbox = user.get("unread_mailbox")
            print(f"to est {user.get('unread_mailbox')}")
            all_unread_mailbox.append({'user':user.get("user",''), 'unread_mailbox': unread_mailbox})
            print(f"to jest w all_unread_mailbox: {all_unread_mailbox}")
            print(f"to jest dlugosc {len(all_unread_mailbox)}")
            user.get("mailbox").extend(unread_mailbox)
            user['unread_mailbox'] = list()
        with open("test_database.json", 'w') as db:
            json.dump(json_database, db) 
        for user in all_unread_mailbox:
            print("-------")
            print(user)
    return all_unread_mailbox



def add_user_to_database(user, password):
    with open ('test_database.json', 'r') as db:
        json_database = json.load(db)
    if len(json_database.get('users','')) < 1:
        json_database['users'].append({'user': user, 'password':password, "mailbox": list(), 'unread_mailbox':list(), 'admin': True})
    else:
        json_database['users'].append({'user': user, 'password':password, 'mailbox': list(), 'unread_mailbox':list(), 'admin': False})
    
    with open("test_database.json", "w") as db:
        json.dump(json_database, db)        

def change_password_in_user_database(username, password):
    with open ('database.json','r') as db:
        json_database = json.load(db)
    for user in json_database.get("users",''):
        if username == user.get("user",''):
            user['password'] = password
            with open("database.json", "w") as db:
                json.dump(json_database, db) 
            return True
        else:
            return False

def authorize_user(username, password):
    with open ('database.json','r') as db:
        json_database = json.load(db)

    for user in json_database.get('users',''):
        print(f"username: {username}, password: {password}")
        print(f" user.get('user','' {user.get('user')} and password: {user.get('password')}")
        if username == user.get('user','') and password == user.get('password',''):
            return True
        

def add_message_to_user_mailbox(username, message):
    with open('database.json','r') as db:
        json_database = json.load(db)

    for user in json_database.get("users",''):
        if username == user.get("user",''):
            if len(user.get("unread_mailbox",''))< 5:
                user.get("unread_mailbox",'').append(message)
                with open("database.json", "w") as db:
                    json.dump(json_database, db) 
                return True
            else:
                return False
