from datetime import datetime
import time
import socket as soc
import json
from datetime import datetime
from connection import Connection
from database import change_password_in_user_database, check_if_user_exists_in_database, add_message_to_user_mailbox, check_queryset_in_the_database ,create_databse, add_user_to_database, authorize_user
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
                    mail_content = data.get("mail_content",'')
                    recipent = data.get("recipent",'')

                    if add_message_to_user_mailbox(username=recipent, message=mail_content):
                        message='Your mail has been sent'
                        sc.send_json(message)
                    else:
                        message = "Mailbox of your recipent is full!"
                        sc.send_json(message)

                case "change_password":
                    user = data.get("user",'')
                    password = data.get("password",'')
                    if change_password_in_user_database(user, password):
                        message = 'password has been changed'
                        sc.send_json(message)
                    else:
                        message = "something went wrong!"
                        sc.send_json(message)
                    
                case other:
                    message = "there is not such command available"
                    sc.send_json(message)

main()
