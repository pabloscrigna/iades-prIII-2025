import socket


# datos servidor
host = "localhost"     # 127.0.0.1
port = 5081

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

client_socket.send(b"Soy Pablo")

datos = client_socket.recv(1024)

datos_decode = datos.decode()

print("hora: ", datos_decode)

client_socket.close()