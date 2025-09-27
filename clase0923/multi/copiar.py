"""
python3 copiar.py origen destino
"""
import multiprocessing
import sys


def copiar(origen, destino):
    
    try:
        with open(origen, "r") as file_origen:
            datos = file_origen.read()
    except FileNotFoundError:
        print(f"Archivo {origen} no valido")
        return False
    
    with open(destino, "w") as file_destino:
        file_destino.write(datos)

    
    return True


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("error")


    # Cual es mi archivo origen y mi archivo destino

    origen = sys.argv[1]
    destino = sys.argv[2]

    proceso_copia = multiprocessing.Process(target=copiar, args=(origen, destino))
    proceso_copia.start()
    proceso_copia.join()    

    # resultado = copiar(origen, destino)
    # if resultado:
    #     print(f"origen: {origen} -- destino: {destino} se copio exitosamente")
    #     exit(0)
# 
    # print("Error al copiar")
    # exit(1)
