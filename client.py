from connection import Connection
 

client = Connection(connection_type='CLIENT')

with client as c:
    
    while True:
        choice = input("What wuould you like to do?: ")
        if choice == "stop":
            c.send_json(choice)
            break
        c.send_json(choice)
        data = c.recv_data()
        print(data)
