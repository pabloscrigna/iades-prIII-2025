
"""
Vamos a crear un usuario y un Tweet para ese usuario
"""

from models import User, Tweet


user = User.get(User.username == "avaquero")

print(f"Usuario: {user.username}  ID: {user.id}")


try:
    user = User.get(User.username == "gvaquero")
    print(f"Usuario: {user.username}  ID: {user.id}")
except User.DoesNotExist:
    print("Usuario no encontrado")

tweet =  Tweet.create(user="pscigna", message="Hola mundo!!!")




