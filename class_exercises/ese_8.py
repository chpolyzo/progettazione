'''
Date due coordinate genera una
lista di coordinate con x y assegnandoli il nome
e trovare il massimo delle x e il massimo delle y
'''

class Punto(object):

    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
        self.nome = ""

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_nome(self):
        return self.nome

    def set_nome(self, nome_punto):
        self.nome = nome_punto

lista_punti = []
print("vuoi inserire un punto s/n?")
comando = input(">> inserisci il comando:")
while comando!='n':
    x = int(input(">> inserisci coordinata x:"))
    y = int(input(">> inserisci coordinata y:"))
    nome = input(">> inserisci il nome del punto")
    nuovo_punto = Punto(x,y)
    nuovo_punto.set_nome(nome)
    lista_punti.append(nuovo_punto)
    comando = input(">> inserisci il comando:")
print("Programma terminato")