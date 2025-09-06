"""
Distinct: muestra unicos no repetidos. 
"""
import os

from dotenv import load_dotenv
from time import sleep
from pymongo import MongoClient, ASCENDING, DESCENDING


load_dotenv()  # Load environment variables from .env file

mongo_url = os.getenv("MONGODB_URI")   # string conexion

try:
    client = MongoClient(host=mongo_url)
except Exception as e:
    print(e)
    exit(1)

DB = "iades"
COLLECTION = "precios_surtidor"

# DB
db_iades = client[DB]
collection = db_iades[COLLECTION]

# listar todos los objetos de mi coleccion
query = {"idempresa": 10677}

cantidad = collection.count_documents(query)
limit = 5
skip = 0

while(cantidad > skip):
    cursor = collection.find(query).limit(limit).skip(skip).sort("precio", ASCENDING)
    for objeto in cursor:
        print("Objeto: ", objeto.get("precio"))

    print("skip", skip)
    skip += limit
    sleep(5)


# Cierra la conexion a la DB
client.close()
