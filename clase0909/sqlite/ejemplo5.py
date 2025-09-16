"""
Eliminar registros
"""

from models import User, Tweet

# Eliminar un registro (instancia)
user = User.get(User.username == "elmago")
user.delete_instance()

# Eliminar con query directa
User.delete().where(User.username == "new_user").execute()

# Eliminar todos
# Tweet.delete().execute()