
"""
Vamos a crear un usuario y un Tweet para ese usuario
"""

from models import User, Tweet

user = User(username="avaquero1")
user.save()

tweet = Tweet.create(user="avaquero", message="Primer mensaje!!!" )






