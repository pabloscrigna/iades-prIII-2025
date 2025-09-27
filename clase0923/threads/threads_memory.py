import threading


contador = 0


def incrementador(nombre):
    global contador

    for _ in range(1000):
        contador += 1
    
    print(f"hilo: {nombre} fin")



# Crear los hilos
hilo1 = threading.Thread(target=incrementador, args=("Tarea hilo 1"))
hilo2 = threading.Thread(target=incrementador, args=("Tarea hilo 2"))

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Eseperar que terminen los hilos
hilo1.join()
hilo2.join()

print("Fin de los dos hilos")
