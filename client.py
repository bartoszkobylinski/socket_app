from connection import Connection
 

client = Connection(connection_type='CLIENT')

with client as c:
    
    while True:
        choice = input("What wuould you like to do?: ")

        c.send_json(choice)
        data = c.recv_data()
        print(data)

