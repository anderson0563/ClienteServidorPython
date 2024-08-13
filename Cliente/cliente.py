from socket import *

HOST, PORT = "127.0.0.1", 40000

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"IME Brasil!")
    data = s.recv(1024)

print(f"Received {data!r}")