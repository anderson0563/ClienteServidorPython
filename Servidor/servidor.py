from socket import *

HOST, PORT = "127.0.0.1", 40000

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Endereço do Cliente {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)