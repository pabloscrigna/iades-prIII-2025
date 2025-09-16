# insert

from models import User, Tweet, db


# conexion a la base
db.connect()

# crea las tablas, safe=True si existen no las crea
db.create_tables([User, Tweet], safe=True)

user = User(username="elmagico")

print(f"usuario: {user.username}")

user.save()

# When a model has a foreign key, you can directly assign a model instance
# to the foreign key field when creating a new record.

tweet = Tweet.create(user="pscrigna", message='River!!!')

# If you simply wish to insert data and do not need to create a model instance,
# you can use

user_pk = User.insert(username='new_user').execute()