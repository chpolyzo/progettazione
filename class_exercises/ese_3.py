'''
Date le misure a e b di un rettangolo potenziale
(a e b possono essere nulle o negative) si vuole
sapere si tratta di un quadrato, di un rettangolo, di
un segmento, di un punto o di un caso impossibile
'''

a=input("Inserisci il valore di A")
b=input("Inserisci il valore di B")
print("Il valore di A è: "+str(a))
print("Il valore di B è: "+str(b))
a = int(a)
b = int(b)
if a<0 or b<0:
    print("CASO IMPOSSIBILE!")
elif a==0 and b==0:
    print("SI TRATTA DI UN PUNTO!")
elif a==0 or b==0:
    print("SI TRATTA DI UN SEGMENTO!")
elif a != b:
    print("SI TRATTA DI UN RETTANGOLO!")
else:
    print("SI TRATTA DI UN QUADRATO")
