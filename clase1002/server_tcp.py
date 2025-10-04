import time
import socket

# Creamos un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Variables asociadas al servidor 
host = '0.0.0.0'
port = 5081

server_socket.bind((host, port))

server_socket.listen()

print("Servidor escuchando....")


while True:
    
    client_socket, client_address = server_socket.accept()
    
    print(f"Se conecto:  {client_address}")
    # datos recibidos
    datos = client_socket.recv(1024)
    print("datos:", datos.decode())

    fecha_hora = time.strftime('%Y-%m-%d-%H:%M')

    client_socket.send(fecha_hora.encode())
    client_socket.close()




