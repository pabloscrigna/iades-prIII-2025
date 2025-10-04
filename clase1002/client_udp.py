import socket


# datos servidor
host = "localhost"     # 127.0.0.1
port = 5081

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto(b"Hola server UDP", (host, port))

hora, _ = client_socket.recvfrom(1024)

print(hora.decode())