class Impiegato(object):

    def __init__(self):
        self.nome = ''
        self.cognome = ''
        self.matricola = ''
        self.stipendio = 0

    def set_dettagli(self, name, lastname, impiegato_id, wage):
        self.nome = name
        self.cognome = lastname
        self.matricola = impiegato_id
        self.stipendio = wage

    def get_dettagli(self):
        return self.nome, self.cognome, self.matricola, self.stipendio

    def aumenta_stipendio(self):
        return self.stipendio * 1.1

    def stampa_dettagli(self):
        print("Nome: {0}".format(self.nome))
        print("Cognome: {0}".format(self.cognome))
        print("Matricola: {0}".format(self.matricola))
        print("Stipendio: {0}".format(self.stipendio))


def comando_menu():
    comandi = {
        "Scegli un'operazione:": '',
        "Aggiungi impiegato": '- 1',
        "Aumenta stipendio di tutti": '- 2',
        "Aumenta stipendio singolo": '- 3',
        "Stampa lista impiegati": '- 4',
        "Esci": '- 5'
    }
    for v, k in comandi.items():
        print(v, k)

    comando = input("\nInserisci ora il comando:\n")
    return comando

def aggiungi_impiegato(lista_impiegati):
    nome = input("Inserisci nome:")
    cognome = input("Inserisci cognome:")
    matricola = input("Inserisci matricola:")
    stipendio = int(input("Inserisci stipendio:"))
    oggetto = Impiegato()
    oggetto.set_dettagli(nome, cognome, matricola, stipendio)
    oggetto.get_dettagli()
    print("\nHai inserito i seguenti dati:")
    oggetto.stampa_dettagli()
    lista_impiegati.append(oggetto)
    print("La lista impiegati adesso è {0}\n".format(lista_impiegati))
    return oggetto

def aumenta_tutti_stipendi(lista_impiegati):
    for impiegato in lista_impiegati:
        impiegato.aumenta_stipendio()
        print("Lo stipendio ora è {0}:".format(impiegato.aumenta_stipendio()))


def trova_e_aumenta(impiegato, lista_impiegati):
    matricola = input("Cerca matricola:")
    print(lista_impiegati)
    try:
        print("La matricole è {}".format(impiegato.matricola) if impiegato.matricola == matricola)
        impiegato.aumenta_stipendio()
        print("Stipendio Aumentato\n")
    except ValueError:
        print("L'utente cercato non esiste")

def stampa_lista(lista_impiegati):
    for impiegato in lista_impiegati:
        impiegato.stampa_dettagli()

def salva_lista_in_file(lista_impiegati):
    with open("impiegati.txt", "wb") as f:
        for i_object in lista_impiegati:
            pickle.dump(i_object, f)
            print("Oggetto salvato correttamente")

def appendi_file_impiegati(impiegato, lista_impiegati):
    with open("impiegati.txt", "rb") as f:
        lista_impiegati.append(impiegato)

def crea_file_se_non_esiste(file_path):
    try:
        with open(file_path, "a+") as file:
            pass  # file esistente
    except FileNotFoundError:
        with open(file_path, "w+") as file:
            pass  # crea file

import pickle
file_path = './impiegati.txt'


lista_impiegati = []
crea_file_se_non_esiste(file_path)
comando = comando_menu()
dict_funzioni = {"1":aggiungi_impiegato,
                 "2":aumenta_tutti_stipendi,
                 "4":stampa_lista}
while comando != "5":
    funzione_selezionata = dict_funzioni.get(comando)
    try:
        funzione_selezionata
        funzione_selezionata(lista_impiegati)
    except:
        trova_e_aumenta(oggetto, lista_impiegati)
    finally:
        print("Inserisci un comando valido")
    salva_lista_in_file(lista_impiegati)
    comando = comando_menu()
