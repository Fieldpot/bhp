# -*- coding: utf-8 -*-

import socket

target_host = "0.0.0.0"
target_port = 9999

# ソケットオブジェクトの作成
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# サーバへの接続
client.connect((target_host,target_port))

#  データの送信
request_message ="GET / HTTP/1.1\r\nHost: google.com\r\n\r\n" 
client.send(request_message.encode())

# データの受信
response = client.recv(4096)

print(response.decode())
