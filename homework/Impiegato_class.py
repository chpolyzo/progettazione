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
        print(self.nome)
        print(self.cognome)
        print(self.matricola)
        print(self.stipendio)


def comando_menu():
    comandi = {
        0: "Scegli un'operazione:",
        1: "Aggiungi impiegato: 1",
        2: "Aumenta stipendio di tutti: 2",
        3: "Aumenta stipendio singolo: 3",
        4: "Stampa lista impiegati: 4",
        5: "Esci: 5"
    }
    for c in comandi:
        print(comandi.get(c))

    comando = input("Inserisci ora il comando:")
    return comando


lista_impiegati = []
comando = comando_menu()
while comando != "5":
    if comando == "1":
        # aggiungi impiegato
        nome = input("Inserisci nome:")
        cognome = input("Inserisci cognome:")
        matricola = input("Inserisci matricola:")
        stipendio = int(input("Inserisci stipendio:"))
        oggetto = Impiegato()
        oggetto.set_dettagli(nome, cognome, matricola, stipendio)
        oggetto.get_dettagli()
        print("\nHai inserito i seguenti dati:")
        oggetto.stampa_dettagli()
        print("\n")
        lista_impiegati.append(oggetto)
    elif comando == "2":
        # aumenta tutti gli stipendi
        for elemento in lista_impiegati:
            elemento.aumenta_stipendio()
    elif comando == "3":
        # aumenta uno stipendio
        matricola = input("Cerca matricola:")
        trovato = False
        for elemento in lista_impiegati:
            if elemento.matricola == matricola:
                elemento.aumenta_stipendio()
                trovato = True
        if not trovato:
            print("L'utente cercato non esiste")
        else:
            print("Aumentato")
    elif comando == "4":
        # stampa lista
        for elemento in lista_impiegati:
            elemento.stampa_dettagli()
    else:
        print("Inserisci un comando valido")
    comando = comando_menu()
print("Programma terminato")