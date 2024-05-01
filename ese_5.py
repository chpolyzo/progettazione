'''
Dati n numeri interi calcolare il massimo e
stamparlo
'''

massimo = 0
a = input("Inserisci un numero oppure q: ")
while a!="q":
    a = int(a)
    if a > massimo:
        massimo = a
    a = input("Inserisci un numero oppure q: ")
print("Il massimo numero inserito è: "+str(massimo))
