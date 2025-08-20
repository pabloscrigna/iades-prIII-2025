# exportar a json

#  python       json
#   int          number
#   float       number
#   str         string
#   list       array
#   dict       object
#  
import json

alumnos = {
    "nombre": "pedro",
    "edad": 45,
    "colores" : ["rojo", "amarillo"],
    "altura": 1.63,
    "activo" : True
}


alumno_json = json.dumps(alumnos)

print(alumno_json)
print("type alumno_json:" ,type(alumno_json))



