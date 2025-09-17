
"""
Vamos a crear un usuario y un Tweet para ese usuario
"""

from models import User, Tweet


# user = User(username="fgimenez")
# user.save()


# print(f"el id de el usuario {user.username} es  {user.id}")

user = User.get(User.username == "mpanero")

print(f"Usuario: {user.username}  ID: {user.id}")

# User.create(username="directo")
# Tweet.create(user=user.username, message="Directo sin instancia")

tweet = Tweet.get(Tweet.user == user)

print(tweet)

tweets = Tweet.select().where(Tweet.user == user)
print(tweets)
print("Tweets encontrados")
for tweet  in tweets:
    print(f"{tweet.message} -- {tweet.is_published}")





