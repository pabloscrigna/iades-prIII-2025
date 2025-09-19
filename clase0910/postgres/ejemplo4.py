"""
Busqueda paginada
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
db.create_tables([UserLogistica])


# for i in range(10, 100):
#     UserLogistica.create(
#         username=f"test_{i}",
#         email=f"mail_{i}@mail.com"
#     )

# Parametros para paginar
# limit :  cantidad de objetos, registros que queremos que traiga la busqueda
# skip/offset: offset inicial

limit = 10
offset = 0
sort_field = UserLogistica.username
query = UserLogistica.select().limit(limit).offset(offset).order_by(sort_field.desc())

total = UserLogistica.select().count()

print("total de usuarios: ", total)

for user in query:
    print(f"id: {user.id} -- username: {user.username}")