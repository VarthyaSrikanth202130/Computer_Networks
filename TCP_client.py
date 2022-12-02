import socket
HOST = '127.0.0.1'
PORT = 65432
ENCODE = 'utf-8'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print(f"[CONNECTED] connected to server on port {PORT}")
    data = client.recv(1024).decode(ENCODE)
    data = data.split(" ")
    print(f"Date: {data[0]}\nTime: {data[1]}")
