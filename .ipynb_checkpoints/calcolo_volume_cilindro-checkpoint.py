import math

altezza = input("Inserisci altezza: ")
raggio = input("Inserisci raggio: ")

def calcolo_volume(altezza, raggio):
    volume = math.pi * int(raggio)**2 * int(altezza)
    print("Il volume è {0}".format(volume))

calcolo_volume(altezza, raggio)

