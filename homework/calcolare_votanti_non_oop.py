def input_numero_persone(messaggio):
    numero = 0
    is_numero_inserito = False # variabile sentinella - variabile flag per il ciclo
    while not is_numero_inserito:
        string_inserita = input(messaggio)
        try:
            numero = float(string_inserita)
            if numero > 0:
                is_numero_inserito = True
            else:
                print("Il numero inserito è negativo, riprova")
        except Exception:
            print ('La stringa inserita non è un numero')
    return numero

def percentuale_votanti(iscritti, votanti):
    return (votanti/iscritti)*100

def percentuale_si(numero_si, votanti):
    return (numero_si/votanti)*100

def percentuale_no(numero_no, votanti):
    return (numero_no/votanti)*100

def stampa_voti(iscritti, votanti, numero_si, numero_no):
    print("La percentuale dei votanti è {0} %".format(round(percentuale_votanti(iscritti, iscritti), 1)))
    print("La percentuale dei votandi si è {0} %".format(round(percentuale_si(numero_si, votanti), 1)))
    print("La percentuale dei votandi no è {0} %".format(round(percentuale_si(numero_no, votanti), 1)))

# iscritti = int(input("Inserisci numero iscritti (numero intero positivo): "))
# votanti = int(input("Inserisci numero votanti (numero intero positivo): "))
# numero_si = int(input("Inserisci numero votanti 'si' (numero intero positivo): "))
# numero_no = int(input("Inserisci numero votanti 'no' (numero intero positivo): "))
# stampa_voti(iscritti, votanti, numero_si, numero_no)

iscritti = input_numero_persone("Inserisci numero iscritti: ")
votanti = input_numero_persone("Inserisci numero votanti: ")
numero_si = input_numero_persone("Inserisci numero si: ")
input_numero_persone("Inserisci numero no: ")
stampa_voti(iscritti, votanti, numero_si, numero_no)