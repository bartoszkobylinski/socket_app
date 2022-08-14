from connection import Connection

import os
file_path = '/Users/bartoszkobylinski/Programming/Python/socket_server/database.json'



client = Connection(connection_type='CLIENT')

def menu():
    print("""
        --------------------------------------------------------------------------
        You can choose between this commands to interact with server:
                - uptime - shows server lifte time
                - info - returning information about server
                - stop - stopping server and client works
                - help - shows available commands 
                - logout - to log out of profile
                - send_mail - to send message to other user
                - read_mail - to check your mailbox 
                - change_password - to change password as long you have admin rights
                - read_all_mails - to check all unreaded_mails
                - change_user_password - to change password for user
                - create_user - to create a user
        --------------------------------------------------------------------------
    """)
        




with client as c:
    
    while True:
        menu()
        user_input = input("What would you like to do?: ")
        choice = {'choice':user_input}
        if choice.get('choice','') == "stop":
            c.send_json(choice)
            if os.path.isfile(file_path):
                os.remove(file_path)
            break

        elif choice.get('choice','') == 'create_user':
            name = input("What is your name?: ")
            choice.update(name=name)
            password = input("What password would you like to have?: ")
            choice.update(password=password)
            c.send_json(choice)

        elif choice.get('choice','') == 'login':
            name = input('type in your username to login: ')
            password = input('type in your password to log in: ')
            choice.update(name=name)
            choice.update(password=password)
            c.send_json(choice)
        
        elif choice.get('choice','') == 'change_password':
            user = input("what is your username?: ")
            password = input("please set your new password: ")
            choice.update(password=password, user=user)
            c.send_json(choice)

        elif choice.get('choice','') == 'send_mail':
            recipent = input("To whom you want to send message?: ")
            mail_content = input("Type in your message: ")
            choice.update(recipent=recipent, mail_content=mail_content)
            c.send_json(choice)
        
        elif choice.get('choice', '') == 'read_mail':
            user = input("what is your name")
            choice.update(user=user)
            c.send_json(choice)

        elif choice.get('choice','') == 'read_all_mails':
            c.send_json(choice)

        else:
            c.send_json(choice)

        data = c.recv_data()
        print('\n')
        print(data)
