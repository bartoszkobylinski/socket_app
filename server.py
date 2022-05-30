from datetime import datetime
import time
import socket as soc
import json
from datetime import datetime
from connection import Connection
 
 

def main():
    server = Connection()

    
    with server as sc:
        print(f"Connected by {server.address}")
        while True:
            data = sc.recv_data()
            if not data:
                print("There were some problem with connection. You need to connect again")
                break
            match data:
                case "uptime":
                    message = time.time() - sc.time
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
                case other:
                    print("there is not such command available")

main()