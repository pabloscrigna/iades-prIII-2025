
from models import User, Tweet


usuario = input("Ingresar el usuario: ")


user = User.get(User.username == usuario)

print(f"username: {user.username} -- id: {user.id}")

print("Accediendo a los tweets por User")
if user.tweets:
    for t in user.tweets:
        print(f"mensaje: {t.message} -- publicado: {t.is_published}")


print("Accediendo por Tweets")

tweets = Tweet.select().where(Tweet.user == user.id)

for tweet in tweets:
    print(tweet.message)