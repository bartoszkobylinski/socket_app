
import json


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

def add_user_to_database(user, password):
    with open ('database.json', 'r') as db:
        json_database = json.load(db)
    
    json_database['users'].append({'user': user, 'password':password, "mailbox": list()})
    
    with open("database.json", "w") as db:
        json.dump(json_database, db)        
        
def remove_from_database(data):
    with open('database', 'w') as db: 
        pass

def update_record_in_databe(data):
    with open('database', 'w') as db:
        pass

{
    'users': [
        {'name':'bartek','email':'kal@wp.pl','password':'jOKotas324',
        'admin':True, 'logged':False, "messages":['oeuoe','oeuoeu','oeuoeu']}
    ]
}
