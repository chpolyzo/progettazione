
class Macchina(object):

    def __init__(self):
        self.modello = ""
        self.colore = ""
        self.stato = False

    def vernicia(self, vernice):
        self.colore = vernice

    def nome_modello(self, parametro_modello):
        self.modello = parametro_modello

    def accendi(self):
        self.stato = True

    def spegni(self):
        self.stato = False

    def get_stato(self):
        return self.stato

    def get_colore(self):
        return self.colore