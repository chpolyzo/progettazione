'''
Dati n numeri interi calcolare
il massimo, il minimo e
stamparlo a video usando una lista
'''

def trova_massimo(lista_numeri):
    massimo = 0
    for elemento in lista_numeri:
        if elemento > massimo:
            massimo = elemento
    return massimo

def trova_minimo(lista_numeri):
    minimo = 9999
    for elemento in lista_numeri:
        if elemento < minimo:
            minimo = elemento
    return minimo

# inizio programma
lista = []
a = input("Inserisci un numero oppure q: ")
while a!="q":
    a = int(a)
    lista.append(a)
    a = input("Inserisci un numero oppure q: ")
massimo = trova_massimo(lista)
minimo = trova_minimo(lista)
print("Il massimo numero inserito è: "+str(massimo))
print("Il minimo numero inserito è: "+str(minimo))