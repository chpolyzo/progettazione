# 1: definire una classe Esame
#    proprietà: data, corso, voto

class Esame(object):

    def __init__(self, data, corso, voto):
        self.data = data
        self.corso = corso
        self.voto = voto

    def stampaEsitoEsame(self):
        return "il "+str(self.data)+" ha preso "+str(self.voto)+" in "+str(self.corso)

# 2: definire una classe Studente
#    proprietà: matricola, nome, città, dipartimento, esami
#    metodi: aggiungiEsame(data, corso, voto)
#            stampaListaEsami()

class Studente(object):

    def __init__(self, matricola, nome, citta, dipartimento):
        self.matricola = matricola
        self.nome = nome
        self.citta = citta
        self.dipartimento = dipartimento
        self.esami = []

    def aggiungiEsame(self, data, corso, voto):
        esame = Esame(data, corso, voto)
        self.esami.append(esame)


    def stampaListaEsami(self):
        for esame in self.esami:
            print(self.nome+" che viene da "+self.citta+" "+esame.stampaEsitoEsame())

andrea = Studente("111", "Andrea", "Como", "Inf")
andrea.aggiungiEsame("2024/05/07", "Inf", 30)
andrea.stampaListaEsami()
#OUT: Andrea che viene da Como il 2024/05/07 ha preso 30 in Inf