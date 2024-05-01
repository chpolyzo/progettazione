'''
Dati n numeri interi calcolare
il massimo, il minimo e
stamparlo a video
'''

massimo = 0
minimo = 9999
lista = []
a = input("Inserisci un numero oppure q: ")
while a!="q":
    a = int(a)
    lista.append(a)
    a = input("Inserisci un numero oppure q: ")
for elemento in lista:
    if elemento > massimo:
        massimo = elemento
    if elemento < minimo:
        minimo = elemento
print("Il massimo numero inserito è: "+str(massimo))
print("Il minimo numero inserito è: "+str(minimo))