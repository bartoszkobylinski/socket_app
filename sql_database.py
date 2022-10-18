from database import check_if_user_exists_in_database
from multiprocessing import connection
import psycopg2
from psycopg2 import Error

try:
    db_connection = psycopg2.connect(user='bartoszkobylinski',
    host = '127.0.0.1',
    port = '5432',
    database = 'bartoszkobylinski'
    )   
    cursor = db_connection.cursor()
    print("PostgreSQL serever information")
    print(db_connection.get_dsn_parameters(), '\n')
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
except(Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (db_connection):
        cursor.close()
        db_connection.close()
        print("PostgreSQL connection is closed")

def create_table():
    db_connection = psycopg2.connect(user='bartoszkobylinski',
    host = '127.0.0.1',
    port = '5432',
    database = 'bartoszkobylinski')
    cursor = db_connection.cursor()
    table_creation_query = (''' 
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        user_name VARCHAR (50), 
        password VARCHAR (50), 
        admin BOOLEAN NOT NULL)
    ''',
    '''
    CREATE TABLE mailboxes (
        user_id INTEGER PRIMARY KEY,
        user_name VARCHAR (50),
        message_read BOOLEAN NOT NULL DEFAULT FALSE,
        message VARCHAR (255)
    )
    ''')
    for query in table_creation_query:
        cursor.execute(query)
    
    print("table have been created!")
    cursor.close()
    db_connection.commit()

#create_table()

#database_queries

def check_if_user_already_is_in_postgresql(query):
    db_connection = psycopg2.connect(user='bartoszkobylinski',
    host = '127.0.0.1',
    port = '5432',
    database = 'bartoszkobylinski')
    cursor = db_connection.cursor()
    check_query = f'''SELECT true FROM users WHERE user_name='{query}';'''
    print(f"this is check query: {check_query}")
    cursor.execute(check_query)
    answer = cursor.fetchall()[0][0]
    db_connection.close()
    return answer


def add_username_to_postgresql(username, password, admin):
    if not check_if_user_already_is_in_postgresql(username):
        db_connection = psycopg2.connect(user='bartoszkobylinski',
        host = '127.0.0.1',
        port = '5432',
        database = 'bartoszkobylinski')
        cursor = db_connection.cursor()
        query = '''INSERT INTO users (user_name, password, admin) VALUES (%s, %s, %s)'''
        values = username, password, admin  
        data = cursor.execute(query, values)
        print(f"here is data:{data}")
        db_connection.commit()
        db_connection.close()
    else:
        print("User already exists!")

add_username_to_postgresql('marian','noeuhhkostah.cr', False)
    

def update_query_in_postgresql(query):
    pass
 




def check_if_user_exist_in_postgresql(username):
    pass

def add_user_to_postgresql(username, password):
    pass