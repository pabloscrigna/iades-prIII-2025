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
query = {}
#cursor = collection.find(query)    # lazy 

cantidad = collection.count_documents(query)
print("cantidad: ", cantidad)

print("imprimiendo los primeros 3")
cursor = collection.find(query).limit(3).skip(0).sort("precio", ASCENDING)
for objeto in cursor:
    print("Objeto: ", objeto.get("precio"))

sleep(5)

print("imprimiendo los segundos 3")
cursor = collection.find(query).limit(3).skip(3).sort("precio", ASCENDING)
for objeto in cursor:
    print("Objeto: ", objeto.get("precio"))

# Cierra la conexion a la DB
client.close()
