import os
candidati = ['Pippo', 'Pluto', 'Paperino']

def clearConsole():
    """
    Funzione che ha il solo scopo di pulire il video
    """
    command = "clear"
    os.system(command)

def nuova_operazione():
    """
    Funzione che ha il solo scopo di
    1. visualizzare le varie voci
    2. ricevere l'input dall'utente
    input: NIENTE
    output: la selezione dell'utente
    """
    clearConsole()
    print("Ecco cosa puoi fare:")
    print("1 - Nuova votazione")
    print("2 - Vedi lista votanti")
    print("3 - Risultato votazioni")
    print("4 - Vincitore")
    print("q - Esci")
    carattere = input(">>> Inserisci un comando:")
    clearConsole()
    return carattere


class Persona(object):

    # constructor of the class
    def __init__(self, nome='Privacy please'):
        self.name = nome
        self.voto = ''

    def vota(self, preferenza):
        self.voto = preferenza

    def get_name(self):
        return self.name

    def get_voto(self):
        return self.voto


def inserisci_scelta():
    print("Benvenuto in cabina elettorale!")
    print("Ecco la lista dei candidati")
    for candidato in candidati:
        print(candidato)
    return input("Chi vuoi votare?")


def calcola_statistiche(lista):
    voti_validi = 0
    voti_nulli = 0
    astenuti = 0
    for votante in lista:
        if votante.get_voto() == "":
            astenuti += 1
        elif votante.get_voto() in candidati:
            voti_validi +=1
        else:
            astenuti += 1
    return [voti_validi, voti_nulli, astenuti]


def totale_voti_candidato(candidato, lista):
    voti_candidato = 0
    for persona in lista:
        if persona.get_voto() == candidato:
            voti_candidato += 1
    return voti_candidato


def nomina_vincitore(lista):
    for candidato in candidati:
        voti_candidato = totale_voti_candidato(candidato, lista)
        print("Il candidato "+str(candidato)+ " ha riportato "+str(voti_candidato)+" voti.")


comando = nuova_operazione()
lista_votanti = []
while comando != 'q':
    if comando == "1":
        nome_persona = input("chi sta votando? [invio per anonimato]")
        if len(nome_persona)>0:
            nuovo_oggetto_persona = Persona(nome_persona)
        else:
            nuovo_oggetto_persona = Persona()
        scelta_personale = inserisci_scelta()
        nuovo_oggetto_persona.vota(scelta_personale)
        lista_votanti.append(nuovo_oggetto_persona)
    if comando == "2":
        print("Numero votanti: "+str(len(lista_votanti)))
        for persona in lista_votanti:
            print("---> "+str(persona.get_name()))
    if comando == "3":
        [voti_validi, voti_nulli, astenuti] = calcola_statistiche(lista_votanti)
        print("Numero registrati: "+str(len(lista_votanti)))
        print("Numero voti validi: "+str(voti_validi))
        print("Numero voti nulli: "+str(voti_nulli))
        print("Numero astenuti: " + str(astenuti))
    if comando == "4":
        vincitore = nomina_vincitore(lista_votanti)
        print("Vincitore: " + str(vincitore))
    # la comando non è tra quelle previste
    print("Attenzione, inserisci un comando valido")
    comando = nuova_operazione()
print("Arrivederci")
