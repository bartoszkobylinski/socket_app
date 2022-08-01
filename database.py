
import json


def create_databse():
    with open('database.json', "w") as db:
        print("Database has been created")
        db.write(json.dumps({'users':[]}))

def check_database(data):
    with open ('database.json', 'r') as db:
        pass

def add_to_database(data):
    with open ('database.json', 'a') as db:
        pass
        
        
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
