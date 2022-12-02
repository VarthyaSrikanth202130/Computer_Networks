import socket
from datetime import datetime
HOST = "127.0.0.1"
PORT = 65432
ENCODE = 'utf-8'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Listening on port {PORT}...")
    client, addr = server.accept()
    print(f"[CONNECTED] Connected to {addr}")
    with client:
        data = datetime.now()
        data = str(data).encode(ENCODE)
        client.sendall(data)
        print("Date and time sent successfully...")
