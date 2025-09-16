from peewee import Model, SqliteDatabase, CharField


DB_NAME = "iades_db"

plsql = SqliteDatabase(DB_NAME)


class BaseModel(Model):

    class Meta:
        database = plsql


class User(BaseModel):
    username = CharField(max_length=10)


plsql.connect()
plsql.create_tables([User], safe=True)

username = input("ingresar el nombre de usuario: ")
user = User(username=username)

print("usuario: ", user.username)

# Guarda el usuario user en la tabla User de la DB iades_db
user.save()