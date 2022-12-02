import socket
import time

HOST = "127.0.0.1"
PORT = 65432
ENCODE = 'utf-8'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Listening on port {PORT}...")
    client, addr = server.accept()
    print(f"[CONNECTED] Connected to {addr}")
    try:
        with client:
            while True:
                data = client.recv(1024).decode(ENCODE)
                if data == 'exit':
                    print("Closing the connection...")
                    time.sleep(1)
                    print(
                        f"[DISCONNECTED] connection with client {addr} is closed.")
                    time.sleep(1)
                    print("[SHUTDOWN] server is shutting down.")
                    client.sendall("exit".encode(ENCODE))
                    time.sleep(3)
                    break
                print(f"[{addr}]: {data}")
                data = input(">> ")
                data = data.encode(ENCODE)
                client.sendall(data)
    except Exception as e:
        print(e)
        client.close()
