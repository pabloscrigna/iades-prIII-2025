from models import User


usuario = input("ingrese el usuario: ")

try:
    usuario = User.get(User.username == usuario)
except User.DoesNotExist:
    print(f"Usuario {usuario} inexistente")
    exit(1)

print("usuario seleccionado: ", usuario.username)  

tweets = usuario.tweets

if tweets:
    print("Hay tweets!!!")
    for tweet in tweets:
        tweet.is_published = False
        tweet.message = "Nuevo contenido"
        tweet.save()