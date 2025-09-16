from peewee import Model, SqliteDatabase, CharField


DB_NAME = "iades_db"

plsql = SqliteDatabase(DB_NAME)


class BaseModel(Model):

    class Meta:
        database = plsql


class User(BaseModel):
    username = CharField(max_length=10)


plsql.connect()
plsql.create_tables([User])

tables = plsql.get_tables()

for table in tables:
    print("table: ", table)


