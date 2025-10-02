import asyncio

from time import sleep


# Esta es una funcion
def saludar_sync(nombre: str) -> str:
    sleep(1)  # Simula una operación bloqueante
    return f"Hola, {nombre}!"


# Vamos a hacer una corrutina
async def saludar_async(nombre: str) -> str:
    await asyncio.sleep(4)    
    return f"Corutina --Hola {nombre}"


async def main():
    saludo = await saludar_async("Mica")
    print(saludo)


if __name__ == "__main__":
    #print(saludar_sync("Mundo"))
    asyncio.run(main())
