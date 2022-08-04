import socket as soc
import time
import json
from time import strftime


class Connection:
 
    def __init__(self, host='127.0.0.1', port=6470, buffer=1024, encoder='utf-8', connection_type="SERVER"):
        self.host = host
        self.port = port
        self.buffer = buffer
        self.encoder = encoder
        self.connection_type = connection_type
        self.socket = None
        self.connection = None
        self.address = None
        self.time = None
        self.version = None
 
    def __enter__(self):
        # Setting up server socket and connecting with client
        if self.connection_type == "SERVER":
            self.time = time.time()
            self.socket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen()
            cli_soc, self.address = self.socket.accept()
            self.connection = cli_soc
            self.version = '1.0.0'
        if self.connection_type == "CLIENT":
            self.connection = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
            self.connection.connect((self.host, self.port))
        return self
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        del self
    
    def send_json(self, data):
        package = json.dumps(data, indent=2)
        self.connection.send(package.encode(self.encoder))
 
    def send_raw(self, data):
        self.connection.send(data.encode(self.encoder))
 
    def recv_data(self):
        return json.loads(self.connection.recv(self.buffer).decode(self.encoder))
        
    def info(self):
        server_established_time = strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(self.time))
        return f"Server {self.version} has been established at {server_established_time}."

    def help(self):
        return '''
            You can choose between four commands to interact with server:
            - uptime - shows server lifte time
            - info - returning information about server
            - stop - stopping server and client works
            - help - shows available commands 
            '''

    
    def __str__(self) -> str:
        return f'Server connected at host: {self.host}, port:{self.port} and decode: {self.encoder}'