import multiprocessing
import time
import os


def tarea(nombre, tiempo):
    print(f"Comenzando tarea {nombre} -- PID: {os.getpid()} -- PPID: {os.getppid()}")
    time.sleep(tiempo)
    print(f"Terminando la tarea {nombre}")



if __name__ == "__main__":
    # Crear los procesos
    print(f"PID: {os.getpid()} --- PPID: {os.getppid()}")
    proceso1 = multiprocessing.Process(target=tarea, args=("Tarea proceso 1", 10))
    proceso2 = multiprocessing.Process(target=tarea, args=("Tarea proceso 2", 15))

    # Iniciamos los procesos
    proceso1.start()
    proceso2.start()

    # Eseperar que terminen los procesos
    proceso1.join()
    proceso2.join()

    print("Fin de los dos procesos")