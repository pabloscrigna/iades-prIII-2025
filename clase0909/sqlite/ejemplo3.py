"""
Hacer consultas

"""
from models import User, Tweet

# Obtener un solo registro
user = User.get(User.username == "elmagico")
print(user.id, user.username)

# Filtrar varios
users = User.select().where(User.username.contains("magico"))
for u in users:
    print(u.username)

# Obtener todos
all_users = User.select()



# Obtener todos los tweets
tweets = Tweet.select()
for t in tweets:
    print(f"{t.user.username}: {t.message} ({t.created_date})")


# Todos los tweets de un usuario
tweets = Tweet.select().where(Tweet.user == User.get(User.username == "elmagico"))
for t in tweets:
    print(t.message)

# Tweets que contengan una palabra
tweets = Tweet.select().where(Tweet.message.contains("River"))
for t in tweets:
    print(t.message)



# Tweets más recientes primero
tweets = Tweet.select().order_by(Tweet.created_date.desc())
for t in tweets:
    print(t.message, t.created_date)



# Los 5 primeros
tweets = Tweet.select().limit(5)

# Saltar 5 y traer los siguientes 5
tweets = Tweet.select().offset(5).limit(5)


user = User.get(User.username == "elmagico")
for t in user.tweets:   # backref
    print(t.message)