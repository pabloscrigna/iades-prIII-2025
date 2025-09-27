"""
Ejemplo basco de threads
"""


import threading
from time import sleep


def tarea(nombre, tiempo):
    print(f"Comenzando tarea {nombre}")
    sleep(tiempo)
    print(f"Terminando la tarea {nombre}")


# sin hilos
tarea("Tarea hilo 1", 10)
tarea("Tarea hilo 2", 15)


# Crear los hilos
hilo1 = threading.Thread(target=tarea, args=("Tarea hilo 1", 10))
hilo2 = threading.Thread(target=tarea, args=("Tarea hilo 2", 15))
# 
# # Iniciamos los hilos
hilo1.start()
hilo2.start()
# 
# # Eseperar que terminen los hilos
hilo1.join()
hilo2.join()

print("Fin de los dos hilos")
