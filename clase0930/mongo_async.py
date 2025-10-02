import asyncio
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient


from utils import mongo_url

db_name = "iades-2025"
collection_name = "alumnos"


async def main():

    cliente = AsyncIOMotorClient(mongo_url)
    db = cliente[db_name]
    db_collection = db[collection_name]

    # CREATE
    alumno = {
        "nombre": "Facundo",
        "curso": 6668
    }

    resultado = await db_collection.insert_one(alumno)
    print(f"Se ingreso el id: {resultado.inserted_id}")

    id = resultado.inserted_id
    # find
    alumno = await db_collection.find_one({"_id": ObjectId(id)})

    print(f"alumno: {alumno}")

    await db_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"instituto": "iades-analista"}}
    )
    
    await db_collection.delete_one({"_id": ObjectId(id)})



if __name__ == "__main__":
    asyncio.run(main())
