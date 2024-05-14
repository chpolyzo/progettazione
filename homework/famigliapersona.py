# Definire una classe Persona
# attributi: cf, nome, cognome
# metodi: stampaInfo(), --> "Masciadri Andrea CF: xxxxx"

# Definire una classe Famiglia
# attributi: listaPersone
# metodi: aggiungiPersona(persona)
#       stampaInfo() --> stampa le info di tutti i familiari


class Persona(object):
    def __init__(self, nome, cognome, CF):
        self.nome = nome
        self.cognome = cognome
        self.CF = CF


    def stampaInfo(self):
        print("Nome: {}".format(self.nome))
        print("Cognome: {}".format(self.cognome))
        print("CF: {}".format(self.CF))

class Famiglia(object):

    def __init__(self):
        self.lista_persone = []

    def aggiungiPersona(self, persona):
        self.lista_persone.append(persona)

    def stampaInfo(self):
        for persona in self.lista_persone:
            print("Nome: {}".format(persona.nome))
            print("Cognome: {}".format(persona.cognome))
            print("Codice Fiscale: {}".format(persona.CF))


p = Persona("xxxxxx", "Andrea", "Masciadri")
f = Famiglia()
f.aggiungiPersona(Persona("Dante","Alighieri","23455"))
f.aggiungiPersona(Persona("Camillo","Benso Conte di Cavur","3456"))
f.aggiungiPersona(p)
f.stampaInfo()
