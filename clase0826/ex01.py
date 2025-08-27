import os

from pymongo import MongoClient

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

mongo_url = os.getenv("MONGODB_URI")   # string conexion

try:
    client = MongoClient(host=mongo_url)
    response = client.server_info()
    print(response)
except Exception as e:
    print(e)
    exit(1)

print("Listando Base de datos")
print(client.list_database_names())

DB = "iades"

db_iades = client[DB]

collections_iades = db_iades.list_collection_names()

for collection in collections_iades:
    print("collection: ", collection)

# Cierra la conexion a la DB
client.close()
