class Impiegato(object):

    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio

    def aumenta_stipendio(self):
        self.stipendio = self.stipendio*1.1

    def stampa_dettagli(self):
        print("MATRICOLA "+str(self.matricola)+": "+str(self.cognome)+" "+str(self.nome)+" Stipendio: "+str(self.stipendio)+"€")

def comando_menu():
    print("Scegli una operazione:")
    print("1 - Aggiungi impiegato")
    print("2 - Aumenta stipendio di tutti")
    print("3 - Aumenta stipendio singolo")
    print("4 - Stampa lista impiegati")
    print("5 - esci")
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
        oggetto = Impiegato(nome,cognome,matricola, stipendio)
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