"""
Vamos a crear un usuario y un Tweet para ese usuario
"""

from models import User, Tweet

# Crear usuario si no existe
user, created = User.get_or_create(username="alario")
if created:
    print(f"Usuario nuevo creado: {user.username} (id={user.id})")
else:
    print(f"Usuario ya existente: {user.username} (id={user.id})")

# Crear un tweet para ese usuario
tweet = Tweet.create(user=user, message="Tweet de prueba para fgimenez")
print(f"Tweet creado: {tweet.message} -- publicado={tweet.is_published}")

# Buscar un tweet cualquiera del usuario
try:
    tweet = Tweet.get(Tweet.user == user)
    print(f"Primer tweet encontrado: {tweet.message}")
except Tweet.DoesNotExist:
    print("El usuario no tiene tweets todavía.")

# Buscar todos los tweets del usuario
tweets = Tweet.select().where(Tweet.user == user)

print("Tweets encontrados:")
for t in tweets:
    print(f"{t.message} -- {t.is_published}")




