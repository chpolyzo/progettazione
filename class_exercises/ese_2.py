import os
candidati = ['Pippo', 'Pluto', 'Paperino']

def clearConsole():
    print("############################")
    print()
    print()
    #command = "clear"
    #os.system(command)

def nuova_operazione():
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
        self.nome = nome
        self.xy = '' # l'attributo xy della classe persona conterrà il cod. fisc.
        self.voto = ''

    def effettua_votazione(self, preferenza):
        self.voto = preferenza

    def come_si_chiama(self):
        return self.nome

    def cosa_ha_votato(self):
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
        # NUOVA VOTAZIONE
        nome_persona = input("chi sta votando? [invio per anonimato]")
        if len(nome_persona)>0:
            nuovo_oggetto_persona = Persona(nome_persona)
        else:
            nuovo_oggetto_persona = Persona()
        scelta_personale = inserisci_scelta()
        nuovo_oggetto_persona.effettua_votazione(scelta_personale)
        lista_votanti.append(nuovo_oggetto_persona)
    elif comando == "2":
        # VEDI LISTA VOTANTI
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
