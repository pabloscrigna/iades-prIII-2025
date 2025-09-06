"""
Delete de un documento
Eliminacion de un documento

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

query = {"_id": ObjectId("68a7b1879f16b9dd12ad7db2")}

deleted_doc = doc_surtidores.delete_one(query)

print("status", deleted_doc)
# Cierra la conexion a la DB
client.close()
