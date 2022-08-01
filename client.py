from connection import Connection
 

client = Connection(connection_type='CLIENT')

def menu(user):
    if user.logged:
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
    else: 
        print("""
        You can choose between this commands to interact with server:
                - uptime - shows server lifte time
                - info - returning information about server
                - stop - stopping server and client works
                - help - shows available commands 
                - login - to log in to your profile
        """)

with client as c:
    
    while True:
        user_input = input("What wuould you like to do?: ")
        choice = {'choice':user_input}
        if choice.get('choice','') == "stop":
            c.send_json(choice)
            break
        elif choice.get('choice','') == 'create_user':
            name = input("What is your name?: ")
            password = input("What password would you like to have?: ")
            c.send_json({'choice':choice,'name': name})
            print("tu bylem")
        print("wyszedlem z petli")
        c.send_json(choice)
        print("tu cos jestem")
        data = c.recv_data()
        print(data)
