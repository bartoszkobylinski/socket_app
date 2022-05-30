import socket as soc
import json
from datetime import datetime
 
 
class Connection:
 
    def __init__(self, host, port, buffer, encoder, connection_type="SERVER"):
        self.host = host
        self.port = port
        self.buffer = buffer
        self.encoder = encoder
        self.connection_type = connection_type
        self.socket = None
        self.connection = None
        self.address = None
        self.version = None
        self.time = datetime.now().time()
 
    def __enter__(self):
        # Setting up server socket and connecting with client
        if self.connection_type == "SERVER":
            self.version = '1.0.0'
            self.socket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen()
            cli_soc, self.address = self.socket.accept()
            self.connection = cli_soc
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

    def server_last(self):
        return self.time
    
    def __str__(self) -> str:
        return f'Server connected at host: {self.host}, port:{self.port} with buffer: {self.buffer} and decode: {self.encoder}'

user_choice = input("Your server has been started. Would you like to stop it? If yes choose q: ")
while (input != 'q'):
    server = Connection(host='127.0.0.1', port=1875, buffer=1024, encoder='utf-8')
    client = Connection(host='127.0.0.1', port=1875, buffer=1024, encoder='utf-8', connection_type="CLIENT")
    try:
        print(server)
        print(client)
    except Exception as e:
        print(f"to jest {e}")
    
    print(client.server_last())

    json_sent = client.send_raw(1204)
    print(json_sent)
    

