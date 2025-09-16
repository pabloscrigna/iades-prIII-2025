"""
Actualizar 
"""

from models import User

# Opción 1: sobre una instancia
user = User.get(User.username == "elmagico")
user.username = "elmago"
user.save()   # UPDATE en la DB

# Opción 2: con query directa
User.update(username="elmago").where(User.username == "elmagico").execute()