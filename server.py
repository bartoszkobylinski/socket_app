import socket
from datetime import datetime, timedelta

'''HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

'''
# "uptime" - zwraca czas życia serwera
# "info" - zwraca numer wersji serwera, datę jego utworzenia
# "help" - zwraca listę dostępnych komend z krótkim opisem
# "stop" - zatrzymuje jednocześnie serwer i klienta


class Server:


    def __init__(self, version='1.0.0', HOST='127.0.0.1', PORT=1234):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.version = version
        self.time = datetime.now()
    
    def uptime(self):
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
print(server)
print(f"to jest server.server {server.server}")
print(server.time)
print(server.uptime())
print(server.info())
print(server.help())