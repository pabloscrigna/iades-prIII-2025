
"""
Vamos a crear un usuario y un Tweet para ese usuario
"""

from models import User, Tweet


user = User.get(User.username == "user1")
print(f"Usuario: {user.username}  ID: {user.id}")


try:
    user = User.get(User.username == "user1")
    print(f"Usuario: {user.username}  ID: {user.id}")
except User.DoesNotExist:
    print("Usuario no encontrado")

Tweet.create(user=user, message="Hola mundo!!!")

tweets = Tweet.select().where(Tweet.user == user)

if tweets:
    for tweet in tweets:
        print(tweet.message)
else:
    print("no hay tweets")

