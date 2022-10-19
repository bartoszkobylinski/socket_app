from sqlite3 import connect
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

def connect_to_database():
    db_connection = psycopg2.connect(user='bartoszkobylinski',
    host = '127.0.0.1',
    port = '5432',
    database = 'bartoszkobylinski')
    return db_connection

def create_table():
    database = connect_to_database()
    cursor = database.cursor()
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
    database.commit()

#database_queries

def check_if_user_already_is_in_postgresql(query):
    database = connect_to_database()
    cursor = database.cursor()
    check_query = f'''SELECT true FROM users WHERE user_name='{query}';'''
    print(f"this is check query: {check_query}")
    cursor.execute(check_query)
    answer = cursor.fetchall()[0][0]
    database.close()
    return answer


def add_username_to_postgresql(username, password, admin):
    if not check_if_user_already_is_in_postgresql(username):
        database = connect_to_database()
        cursor = database.cursor()
        query = '''INSERT INTO users (user_name, password, admin) VALUES (%s, %s, %s)'''
        values = username, password, admin  
        cursor.execute(query, values)
        print("User added to database")
        database.commit()
        database.close()
    else:
        print("User already exists!")

def change_user_password_in_postgresql(username, password):
    updated_rows = 0
    database = connect_to_database()
    cursor = database.cursor()
    query = '''UPDATE users SET password = %s WHERE user_name=%s'''
    cursor.execute(query,(username,password))
    # it should be acces to connection for commiting!
    updated_rows = cursor.rowcount
    database.commit()
    database.close()
    return updated_rows

def check_credentials_in_postgresql(username, password):
    database = connect_to_database()
    cursor = database.cursor()
    query = "SELECT * FROM users WHERE user_name = %s;"
    cursor.execute(query,(username,))
    if cursor.rowcount == 1:
        password_from_database = cursor.fetchall()[0][1]
        print(f"is your password {password_from_database}")
        if password == password_from_database:
            return True
        else:
            return False
    else:
        return False


def read_user_mailbox(username):
    db_connection = psycopg2.connect(user='bartoszkobylinski',
        host = '127.0.0.1',
        port = '5432',
        database = 'bartoszkobylinski')
    cursor = db_connection.cursor()
    query = f'''SELECT * FROM mailboxes WHERE user_name='{username}';'''
    cursor.execute(query)
    mails = cursor.fetchall()
    return mails
    

def update_query_in_postgresql(query):
    pass
 




def check_if_user_exist_in_postgresql(username):
    pass

def add_user_to_postgresql(username, password):
    pass