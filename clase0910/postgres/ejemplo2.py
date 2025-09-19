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
db.create_tables([UserNew])


# Ceamos un usuario
username = input("ingresar el nombre de usuario: ")
user = UserNew(username=username)

print("usuario: ", user.username)


# user.create(username="test", email="test@email.com")

user.save()


for user in UserNew.select():
    print(f"username:  {user.username} -- email: {user.email}")

# consulta lazy
users = UserNew.select().where(UserNew.username == "pscrigna")

for user in users:
    print(user.username)


user = UserNew.get(UserNew.username == "pscrigna")

print("usuario: ", user.username)
print("email: ", user.email)

