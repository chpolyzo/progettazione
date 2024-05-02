def input_numero_positivo(messaggio):
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


def calcola_tassa(misura1, misura2):
    COSTANTE_TASSA = 9.3 # questa la useremo come costante
    tassa = misura1 * misura2 * COSTANTE_TASSA
    return tassa


def stampa_tassa(tassa):
    # attenzione: tassa è un numero, per poterlo concatenare bisogna convertirlo in stringa
    print("La tassa da pagare è: {0}".format(round(tassa, 1)))

altezza = input_numero_positivo("Inserisci altezza: ")
larghezza = input_numero_positivo("Inserisci larghezza: ")
tassa = calcola_tassa(altezza, larghezza)
stampa_tassa(tassa)
