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