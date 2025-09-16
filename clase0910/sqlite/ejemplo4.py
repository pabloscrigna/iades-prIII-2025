
"""
Vamos a crear un usuario y un Tweet para ese usuario
"""

from models import User, Tweet

user = User(username="pscrigna")
user.save()

tweet = Tweet.create(user="pscrigna", message="Primer mensaje!!!" )






