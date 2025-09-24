import sys


from time import sleep


print(f"Durmiendo {sys.argv[1]} segundos...")

sleep(int(sys.argv[1])) 

print("Desperté!")