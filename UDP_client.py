import socket
import time
HOST = '127.0.0.1'
PORT = 65432
ENCODE = 'utf-8'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print(f"[CONNECTED] connected to server on port {PORT}")
    try:
        while True:
            data = input(">> ")
            data = data.encode(ENCODE)
            client.sendall(data)
            data = client.recv(1024).decode(ENCODE)
            if data == 'exit':
                print("Closing the connection...")
                time.sleep(1)
                client.sendall("exit".encode(ENCODE))
                print(f"[CLOSED] connection with the server is closed")
                time.sleep(3)
                break
            print(f"[{HOST,PORT}]: {data}")
    except Exception as e:
        print(e)
