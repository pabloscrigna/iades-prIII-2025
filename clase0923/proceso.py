from time import sleep

x = 1

x += 3

with open("archivo.txt", "w") as file:
    file.write(f"El valor de x es: {x}\n")

print(f"El valor de x es: {x}")


exit(1)