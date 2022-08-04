from datetime import datetime
import time
import socket as soc
import json
from datetime import datetime
from connection import Connection
from database import check_if_user_exists_in_database, create_databse, add_user_to_database, authorize_user
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
            print(f"to sa dane odebrane przez server: {data} i typ {type(data)}")
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
                    if check_if_user_exists_in_database(user.name):
                        message = 'User already exists!'
                        sc.send_json(message)
                    else:
                        add_user_to_database(user.name, user.password)
                        message = "New user has been added"
                        sc.send_json(message)
                case "login":
                    user = User(name = data.get('name'), password=data.get('password'))
                    if authorize_user(user.name, user.password):
                        user.logged = True  
                        message = "You've been logged in"
                        sc.send_json(message)
                    else:
                        message = "Something went wrong with authorization. Try log in again"
                        sc.send_json(message)
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
