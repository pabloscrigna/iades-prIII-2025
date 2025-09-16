from datetime import datetime
from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    SqliteDatabase,
    Model,
    TextField
)

DB_NAME = "iades_db"

plsql = SqliteDatabase(DB_NAME)


class BaseModel(Model):

    class Meta:
        database = plsql


class User(BaseModel):
    username = CharField(max_length=10)


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_at = DateTimeField(default=datetime.now())
    is_published = BooleanField(default=True)


plsql.connect()
plsql.create_tables([ User, Tweet], safe=True)