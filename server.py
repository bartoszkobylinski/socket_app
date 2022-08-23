from datetime import datetime
import time
import socket as soc
import json
from datetime import datetime
from connection import Connection
from database import change_password_in_user_database, read_all_user_mailbox, check_if_user_exists_in_database, add_message_to_user_mailbox, create_databse, add_user_to_database, authorize_user, read_user_mailbox
from user import User
from os.path import exists

LOGGED_USERS = []
ADMINS_USERS = []



def main(LOGGED_USERS):
    server = Connection()

    
    with server as sc:
        print(f"Connected by {server.address}")
        database_name = 'database.json'
        database_exists = exists(database_name)
        if not database_exists:
            create_databse(database_name)
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
                    if check_if_user_exists_in_database(user.name):
                        message = 'User already exists!'
                        sc.send_json(message)
                    else:
                        add_user_to_database(user.name, user.password)
                        if len(LOGGED_USERS) <= 1:
                            ADMINS_USERS.append(user.name)
                        message = "New user has been added"
                        sc.send_json(message)
                
                case "read_mail":
                    if LOGGED_USERS:
                        mails = read_user_mailbox(LOGGED_USERS[0])
                        sc.send_json(mails)
                    else:
                        message = 'You have to be logged in to read a mail'
                        sc.send_json(message)
                
                case "login":
                    user = User(name = data.get('name'), password=data.get('password'))
                    if authorize_user(user.name, user.password):
                        LOGGED_USERS.append(user.name)
                        message = "You've been logged in"
                        sc.send_json(message)
                    else:
                        message = "Something went wrong with authorization. Try log in again"
                        sc.send_json(message)
                
                case "read_all_mails":
                    if ADMINS_USERS:
                        mails = read_all_user_mailbox()
                        sc.send_json(mails)
                    else:
                        message = "You cant read mails unless you are an admin"
                        sc.send_json(message)

                case "change_user_password":
                    if ADMINS_USERS:
                        user = data.get("name",'')
                        password = data.get('password','')
                        change_password_in_user_database(username=user, password=password)
                        message = f"Password for {user} has been changed!"
                        sc.send_json(message)
                    else:
                        message = "Something went wrong. Probably you are not an admin"
                        sc.send_json(message)
                
                case "logout":
                    if LOGGED_USERS:
                        LOGGED_USERS.clear()
                    message = 'You have been logged out'
                    sc.send_json(message)

                case "send_mail":
                    if LOGGED_USERS:
                        mail_content = data.get("mail_content",'')
                        recipent = data.get("recipent",'')
                        if len(mail_content) > 255:
                            message = "Your message can't be longer than 255 character"
                            sc.send_json(message)
                        else:
                            if add_message_to_user_mailbox(username=recipent, message=mail_content):
                                message='Your mail has been sent'
                                sc.send_json(message)
                            else:
                                message = "Mailbox of your recipent is full!"
                                sc.send_json(message)
                    else:
                        message = "You have to be logged in to send_mail"
                        sc.send_json(message)

                case "change_password":
                    user = data.get("user",'')
                    password = data.get("password",'')

                    if not LOGGED_USERS:
                        message = "you have to be logged in to change your password! Please log in"
                        sc.send_json(message)
                    elif LOGGED_USERS[0] == user:
                        if change_password_in_user_database(user, password):
                            message = 'password has been changed'
                            sc.send_json(message)
                        else:
                            message = "something went wrong!"
                            sc.send_json(message)
                    else:
                        message = "you have to be logged in to change your password! Please log in"
                        sc.send_json(message)

                case other:
                    message = "there is not such command available"

                    sc.send_json(message)

main(LOGGED_USERS=LOGGED_USERS)
