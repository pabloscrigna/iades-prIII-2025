import datetime
from peewee import (
                    SqliteDatabase,
                    Model,
                    CharField,
                    ForeignKeyField,
                    TextField,
                    DateTimeField,
                    BooleanField
                )


db = SqliteDatabase('../my_app.db')


# Modelos
class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)