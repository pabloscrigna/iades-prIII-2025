
"""
Vamos a crear un usuario y un Tweet para ese usuario
"""

from models import User, Tweet

user = User(username="user1")
user.save()

tweet = Tweet.create(user="user1", message="Primer mensaje!!!" )


