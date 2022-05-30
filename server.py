from datetime import datetime
import time
import socket as soc
import json
from datetime import datetime
from connection import Connection
 
 




def uptime(server):
    print(f"this is type of {type(datetime.now().time())} and value of {datetime.now().time()}")
    print(f"This is type of server.time {type((server.time))} and value of {server.time}")
    print(f"that is your server time: {time.time()-server.time}")
    return time.time()-server.time
    #return datetime.combine(datetime.now()) - datetime.combine(server.time)

def info(server):
    return("""
    Server's creation time: {server.time}
    Server version: {server.version} 
    """)
def help():
    return('''
    You can choose between four commands to interact with server:
    - uptime - shows server lifte time
    - info - returning information about server
    - stop - stopping server and client works
    - help - shows available commands 
    ''')

def main():
    server = Connection(host='127.0.0.1', port=1598, buffer=1024, encoder='utf-8')

    
    with server as sc:
        print(f"Connected by {server.address}")
        while True:
            data = sc.recv_data()
            if not data:
                break
            choice = input("What would you like to do")
            match choice:
                case "uptime":
                    print(uptime(sc))
                    
                case "info":
                    return info(sc)
                case "help":
                    help()
                case "stop":
                    print("Server disconnecting...")
                    break
                case other:
                    print("there is not such command available")

main()