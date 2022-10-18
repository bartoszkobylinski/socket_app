import json


def create_databse(name):
    with open(name, "w") as db:
        print("Database has been created")
        db.write(json.dumps({'users':[]}))

def check_if_user_exists_in_database(username, database_name = 'database.json'):
    with open (database_name, 'r') as db:
        json_database = json.load(db)
    for user in json_database.get("users",''):
        if username == user.get("user",''):
            return True
        else:
            return False
    
def read_user_mailbox(username, database_name = 'database.json'):
    mailbox_to_show = list()
    with open(database_name,'r') as db:
        json_database = json.load(db) 
        for user in json_database.get("users",''):
            if username == user.get("user",''):
                unread_mailbox = user.get("unread_mailbox")
                mailbox_to_show = unread_mailbox
                user.get("mailbox").extend(unread_mailbox)
                user["unread_mailbox"] = list()
        with open(database_name, 'w') as db:
            json.dump(json_database, db)  
    return mailbox_to_show

def read_all_user_mailbox(database_name = 'database.json'):
    with open (database_name,'r') as db:
        all_unread_mailbox = list()
        json_database = json.load(db)
        print(f"to zawartosc bazy danych: {json_database}")
        for user in json_database.get("users",''):
            unread_mailbox = user.get("unread_mailbox")
            print(f"to jest zawartosc unread_mailbox: {unread_mailbox}")
            all_unread_mailbox.append({'user':user.get("user",''), 'unread_mailbox': unread_mailbox})
            user.get("mailbox").extend(unread_mailbox)
            user['unread_mailbox'] = list()
            print(f"to jest zawartosc all_unread_mailbox: {all_unread_mailbox}")
        with open(database_name, 'w') as db:
            json.dump(json_database, db) 
    return all_unread_mailbox



def add_user_to_database(user, password, database_name = 'database.json'):
    with open (database_name, 'r') as db:
        json_database = json.load(db)
    if len(json_database.get('users','')) < 1:
        json_database['users'].append({'user': user, 'password':password, "mailbox": list(), 'unread_mailbox':list(), 'admin': True})
    else:
        json_database['users'].append({'user': user, 'password':password, 'mailbox': list(), 'unread_mailbox':list(), 'admin': False})
    
    with open(database_name, "w") as db:
        json.dump(json_database, db)        

def change_password_in_user_database(username, password, database_name = 'database.json'):
    with open (database_name,'r') as db:
        json_database = json.load(db)
    for user in json_database.get("users",''):
        if username == user.get("user",''):
            user['password'] = password
            with open(database_name, "w") as db:
                json.dump(json_database, db) 
            return True
        else:
            return False

def authorize_user(username, password, database_name = 'database.json'):
    with open (database_name,'r') as db:
        json_database = json.load(db)

    for user in json_database.get('users',''):
        print(f"username: {username}, password: {password}")
        print(f" user.get('user','' {user.get('user')} and password: {user.get('password')}")
        if username == user.get('user','') and password == user.get('password',''):
            return True
        

def add_message_to_user_mailbox(username, message, database_name = 'database.json'):
    with open(database_name,'r') as db:
        json_database = json.load(db)

    for user in json_database.get("users",''):
        if username == user.get("user",''):
            if len(user.get("unread_mailbox",''))< 5:
                user.get("unread_mailbox",'').append(message)
                with open(database_name, "w") as db:
                    json.dump(json_database, db) 
                return True
            else:
                return False
