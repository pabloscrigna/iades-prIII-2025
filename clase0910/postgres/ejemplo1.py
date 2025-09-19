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


class User(BaseModel):
    username = CharField(unique=True, max_length=10)
    email = CharField(default="")


db.connect()
db.create_tables([User])