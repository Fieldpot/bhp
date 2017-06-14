# -*- coding: utf-8 -*- 
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print('[*] Listening on {ip}:{port}'.format(ip = bind_ip, port = bind_port))

# クライアントからの接続を処理するスレッド
def handle_client(client_socket):
    
    # クライアントが送信してきたデータを表示
    request = client_socket.recv(1024)

    print('[*] Received: {data}'.format(data = request.decode()))

    # パケットの返送
    client_socket.send("ACK!".encode())

    client_socket.close()

while True:

    client,addr = server.accept()

    print('[*] Accepted connection from: {addr0}:{addr1}'.format(addr0 = addr[0], addr1 = addr[1]))
    # 受信データを処理するスレッドの起動

    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

