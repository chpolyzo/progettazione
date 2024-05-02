class Saluto(object):

    def __init__(self):
        self.saluto = ''

    def set_saluto(self, ciao):
        self.saluto = ciao

    def get_saluto(self):
        return self.saluto

lista_saluti = []
print("Vuoi inserire un saluto s/n")
comando = input(">> inserisci il comando:")
while comando!='n':
    ciao = input(">> inserisci il saluto che desideri:")
    nuovo_saluto = Saluto()
    nuovo_saluto.set_saluto(ciao)
    nuovo_saluto.get_saluto()

    lista_saluti.append(nuovo_saluto)
    comando = input(">> inserisci il comando:")
print("Programma terminato")

