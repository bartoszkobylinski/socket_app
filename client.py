from connection import Connection
 

client = Connection(connection_type='CLIENT')

def menu(user=None):
    if user is None: 
        print("""
        You can choose between this commands to interact with server:
                - uptime - shows server lifte time
                - info - returning information about server
                - stop - stopping server and client works
                - help - shows available commands 
                - login - to log in to your profile

        """)
    elif user.logged:
        print("""
        You can choose between this commands to interact with server:
                - uptime - shows server lifte time
                - info - returning information about server
                - stop - stopping server and client works
                - help - shows available commands 
                - logout - to log out of profile
                - send_mail - to send message to other user
                - check_mail - to check your mailbox
                - change_pass - to change password as long you have admin rights
        """)
    elif user.logged and user.admin:
        print("cos tam")

with client as c:
    
    while True:
        menu()
        user_input = input("What would you like to do?: ")
        choice = {'choice':user_input}
        if choice.get('choice','') == "stop":
            c.send_json(choice)
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
        else:
            c.send_json(choice)
        data = c.recv_data()
        print(data)
