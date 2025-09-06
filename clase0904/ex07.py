"""
ABM (Alta, Baja, Modificación)
Actualizacion --- Update one


"""
import os

from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient


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

# collection
doc_surtidores = db_iades[COLLECTION]

query = {"_id": ObjectId("68a7b1d09f16b9dd12adb14d")}

update_values = {
    "idempresa": 901090,
    "empresa": "Vasco SRL"
    }

updated_doc = doc_surtidores.update_one(query, {"$set": update_values})

print(updated_doc)

print("documentos afectados:", updated_doc.matched_count)
print("documentos modificados:", updated_doc.modified_count)

# Cierra la conexion a la DB
client.close()
