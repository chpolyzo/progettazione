'''
Dati tre numeri interi calcolare il massimo e
stamparlo
'''


a = input("inserisci a: ")
b = input("inserisci b: ")
c = input("inserisci c: ")
a = int(a)
b = int(b)
c = int(c)
if a>b and a>c:
    print("A è il maggiore e vale: "+str(a))
elif b>a and b>c:
    print("B è il maggiore e vale: "+str(b))
else:
    print("C è il maggiore e vale: "+str(c))