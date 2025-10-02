from time import sleep, time


def tareas_sync(nombre, duracion):
    sleep(duracion)
    print(f"sync --- tarea {nombre}")


def ejecutar_sync():

    inicio = time()

    tareas_sync("Tarea 1", 5)
    tareas_sync("Tarea 2", 10)

    fin = time()

    print(fin - inicio)


if __name__ == "__main__":
    ejecutar_sync()
