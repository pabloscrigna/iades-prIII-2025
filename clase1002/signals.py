"""
signals.py
"""
import os
import signal

def signal_handler(sig, frame):
    print(sig)
    entrada = input("Estas seguro de salir de tu programa: s/n ")
    if entrada.lower() == "s":
        print("Saliendo....")
        exit(1)

# SIGINT CTRL-C
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    pid = os.getpid()
    print(pid)
    while(True):
        pass