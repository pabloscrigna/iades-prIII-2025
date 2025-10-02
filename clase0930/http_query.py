import asyncio
import httpx


# asincrono
async def main():
    async with httpx.AsyncClient() as cliente:
        respuesta = await cliente.get("https://www.ole.com.ar")
        print(respuesta.status_code)
        print(respuesta.text)


if __name__ == "__main__":
    # sincrono
    respuesta = httpx.get("https://www.ole.com.ar")
    print(respuesta.status_code)
    print(respuesta.text)

    asyncio.run(main())
