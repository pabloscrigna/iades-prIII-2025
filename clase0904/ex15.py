"""
Cargar informacion en una coleccion con la siguiente estructura:

cursoId: ObjectId
nombre: string
apellido: string
credenciales: {usuario: string, password: string}
activo: boolean
cantidad: number

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
COLLECTION = "cursos_ext"

# DB
db_iades = client[DB]
collection = db_iades[COLLECTION]

# Generar un documento
documento = {
    "cursoId": ObjectId(),
    # "nombre": "C++",       
    "credenciales": {
        "usuario": "jperez",    
        "password ": 12345
    },
    "activo": True
}

# Insertar el documento en la coleccion
resultado = collection.insert_one(documento)
print("Documento insertado con ID:", resultado.inserted_id)

# Cierra la conexion a la DB
client.close()
