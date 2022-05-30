'''
import socket
from socket import socket as soc
from datetime import datetime, timedelta

class Server:
    HOST = '127.0.0.1'
    PORT = 12345

    def __init__(self, version='1.0.0', HOST='127.0.0.1', PORT=1234):
        self.version = version
        self.time = datetime.now()
        self.server = None

    def __enter__(self):
        self.server = soc.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((self.HOST, self.PORT))
        self.listen()
        conn, addr = self.accept()
        with conn:
            print(f"Connected by: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Connection has not been established.")
                    break
                conn.sendall(data)
        
    def __exit__(self, exc_type,exc_val,exc_tb):
        if self.server:
            self.server.close()

    def connect(self):
        
        self.bind((self.HOST, self.PORT))
        self.listen()
        conn, addr = self.accept()
        with conn:
            print(f"Connected by: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    
                    break
                conn.sendall(data)
            
    def uptime(self):
        """
        commond which returns server lifetime
        """
        current_time = datetime.now()
        lifetime = current_time - self.time
        return lifetime      

    def info(self):
        return f"Server has been established at {self.time} and current version is {self.version}"

    def help(self):
        return f"""

        commands list:
        1) uptime - command which returns lifetime of a server
        2) info - command which returns information about lifetime server and current version of it
        3) help - command which returns list of commands available for user 
        4) stop - commmand which stops server and client """

    def stop(self):
        pass

server = Server()
server.__enter__()

#server.connect()
'''
