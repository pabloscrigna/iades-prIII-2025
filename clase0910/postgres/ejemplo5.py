"""
Busqueda por un campo y eliminar la instancia
"""

from peewee import BooleanField, CharField, Model, PostgresqlDatabase


db = PostgresqlDatabase(
    "mydatabase",
    user="myuser",
    password="mypassword",
    host="localhost",      # 127.0.0.1
    port=5432
)


class BaseModel(Model):
    class Meta:
        database = db


class UserLogistica(BaseModel):
    username = CharField(unique=True, max_length=10)
    email = CharField(default="")
    status = BooleanField(default=True)


db.connect()

# Busqueda por username
usuario = input("Ingresar el usuario a borrar")
try:
    user = UserLogistica.get(UserLogistica.username == usuario)
except UserLogistica.DoesNotExist:
    print("Usuario inexistente")
    exit(1)

print("Esta seguro de borrar el usuario ", user.username )

user.delete_instance()

