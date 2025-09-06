"""
ABM (Alta, Baja, Modificación)
Alta

doc = {
  "idempresa": 9409,
  "cuit": "30-71512556-1",
  "empresa": "ALAN S.R.L.",
  "direccion": "AV. 101 Nº 6211 (RUTA 8)",
  "localidad": "MERLO",
  "provincia": "BUENOS AIRES",
  "idproducto": "19",
  "producto": "Gas Oil Grado 2",
  "idtipohorario": "3",
  "tipohorario": "Nocturno",
  "precio": "1378",
  "fecha_vigencia": "2025-08-02 08:30:00",
  "idempresabandera": "28",
  "empresabandera": "PUMA",
  "latitud": "-34.561286",
  "longitud": "-58.588248",
  "geojson": "{\"type\":\"Point\",\"coordinates\":[-58.588248,-34.561286]}"
}

"""
import os

from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()  # Load environment variables from .env file

mongo_url = os.getenv("MONGODB_URI")   # string conexion

try:
    client = MongoClient(host=mongo_url)
    # response = client.server_info()
    # print(response)
except Exception as e:
    print(e)
    exit(1)


DB = "iades"
COLLECTION = "precios_surtidor"

# DB
db_iades = client[DB]

# collection
doc_surtidores = db_iades[COLLECTION]

nuevo_documento = {
  "idempresa": 90000,
  "cuit": "30-71512556-1",
  "empresa": "ALAN S.R.L.",
  "direccion": "AV. 101 Nº 6211 (RUTA 8)",
  "localidad": "MERLO",
  "provincia": "BUENOS AIRES",
  "idproducto": "19",
  "producto": "Gas Oil Grado 2",
  "idtipohorario": "3",
  "tipohorario": "Nocturno",
  "precio": "1378",
  "fecha_vigencia": "2025-08-02 08:30:00",
  "idempresabandera": "28",
  "empresabandera": "PUMA",
  "latitud": "-34.561286",
  "longitud": "-58.588248",
  "geojson": "{\"type\":\"Point\",\"coordinates\":[-58.588248,-34.561286]}"
}

resultado = doc_surtidores.insert_one(nuevo_documento)

doc = doc_surtidores.find_one({"_id": ObjectId(resultado.inserted_id)})

print(f"Documento insertado: {doc}")


# Cierra la conexion a la DB
client.close()
