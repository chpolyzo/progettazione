import math

altezza = int(input("Inserisci altezza (numero intero positivo): "))
raggio = int(input("Inserisci raggio (numero intero positivo): "))
def calcolo_volume(altezza, raggio):
    volume = math.pi * int(raggio)**2 * int(altezza)
    print("Il volume è {0}".format(round(volume, 3)))

calcolo_volume(altezza, raggio)

