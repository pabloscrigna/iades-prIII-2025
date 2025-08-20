# exportar a json

#  python       json
#   int          number
#   float       number
#   str         string
#   list       array
#   dict       object 
# type hints  

import json


def to_json(datos: dict)-> str:
    datos = json.dumps(datos)
    return datos    

def to_dict(data: str)-> dict:
    data = json.loads(data)
    return data


alumnos = {
    "nombre": "pedro",
    "edad": 45,
    "colores" : ["rojo", "amarillo"],
    "altura": 1.63,
    "activo" : True
}


alumno_json = to_json(alumnos)

print(alumno_json)
print("type alumno_json:" ,type(alumno_json))


alumno_dict = json.loads(alumno_json)

print(alumno_dict)
print("type alumno_dict:" ,type(alumno_dict))


frase: str = "Hola mundo!!"

print(frase)


# Archivos

# context manager
with open("datos.json", "w") as file:
    json.dump(alumnos, file) 


with open("datos.json", "r") as file:
    data = json.load(file) 

print("data:", data)