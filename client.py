
import socket as soc
import json
from datetime import datetime
from connection import Connection
 

client = Connection(host='127.0.0.1', port=1598, buffer=1024, encoder='utf-8', connection_type='CLIENT')

with client as client:
    
    while True:
        choice = input("")
    client.send_json('Hello')
    data = client.recv_data()

