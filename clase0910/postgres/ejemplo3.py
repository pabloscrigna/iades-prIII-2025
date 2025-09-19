"""
Conectarse a la DB y actualizar todos emails de los usuarios que no lo tengan cargado
"""

from peewee import CharField, Model, PostgresqlDatabase


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


class UserNew(BaseModel):
    username = CharField(unique=True, max_length=10)
    email = CharField(default="")


db.connect()


# Leer todos los usuarios que tengan el campo email en blanco

users = UserNew.select().where(UserNew.email == "")

if users:
    for user in users:
        print("id: ", user.id)
        print("username: ", user.username)
        print("email: ", user.email)
        email = input("ingresar mail: ")
        user.email = email
        user.save()
else:
    print("Todos los usuarios tienen un email asociado")