import time
import socket

# Creamos un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Variables asociadas al servidor 
host = '0.0.0.0'
port = 5081


server_socket.bind((host, port))

while True:

    data, address = server_socket.recvfrom(1024)
    
    print("data", data.decode())
    print("conexion desde: ", address)

    fecha_hora = time.strftime('%Y-%m-%d-%H:%M')

    server_socket.sendto(fecha_hora.encode(), address)