"""
Distinct: muestra unicos no repetidos. 
"""
import os

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
collection = db_iades[COLLECTION]

# distinct
cursor_distinct = collection.distinct("idproducto")

print("id productos:", cursor_distinct)

# Cierra la conexion a la DB
client.close()
