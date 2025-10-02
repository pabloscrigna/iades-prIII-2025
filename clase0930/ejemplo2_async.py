import asyncio

from time import time


async def tarea_async(nombre, duracion):
    print(f"Tarea: {nombre} -- {duracion}")
    await asyncio.sleep(duracion)
    print(f"sync --- tarea {nombre}")
    return f"Finalizo tarea: {nombre}"


async def main():

    inicio = time()

    lista_tareas = [
        tarea_async("Tarea_1", 5),
        tarea_async("Tarea 2", 15),
        tarea_async("Tarea 3", 5),
    ]

    await asyncio.gather(*lista_tareas)

    fin = time()
    print(f"Duracion: {fin - inicio}")


if __name__ == "__main__":
    asyncio.run(main())
