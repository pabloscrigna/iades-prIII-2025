"""
Vamos a crear una Tabla User con el campo username de tipo CharField
"""
from peewee import SqliteDatabase, Model, CharField

DB_NAME = "base_iades_sqlite"

psql_db = SqliteDatabase(DB_NAME)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db


class User(BaseModel):
    username = CharField()


psql_db.connect()
psql_db.create_tables([User])

tables = psql_db.get_tables()

for table in tables:
    print("tabla: ", table)
