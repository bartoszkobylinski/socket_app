from datetime import datetime
import time
import socket as soc
import json
from datetime import datetime
from connection import Connection
from database import add_to_database, check_database, create_databse
from user import User
from os.path import exists
 

def main():
    server = Connection()

    
    with server as sc:
        print(f"Connected by {server.address}")
        database_exists = exists('database.json')
        if not database_exists:
            create_databse()
        while True:
            data = sc.recv_data()
            if not data:
                print("There were some problem with connection. You need to connect again")
                break
            match data.get('choice',''):
                case "uptime":
                    message = f"{round(time.time() - sc.time, 2)}s"
                    sc.send_json(message)
                case "info":
                    message = sc.info()
                    sc.send_json(message)
                case "help":
                    message = sc.help()
                    sc.send_json(message)
                case "stop":
                    print("Server disconnecting...")
                    break
                case 'create_user':
                    user = User(name = data.get('name'), password=data.get('password'))
                    print(f"User added such information name: {user.name} and password {user.password}.")
                    if not user.name in check_database(user.name):
                        add_to_database(user)
                        print("New user has been added")
                    else:
                        message = "user is already in database. Would you like to login instead of creating user?"
                        sc.send_json(message)
                case "login":
                    pass                    
                case "logout":
                    pass
                case "send_mail":
                    pass
                case "edit user":
                    pass
                case "change password":
                    pass




                case other:
                    message = "there is not such command available"
                    sc.send_json(message)

main()