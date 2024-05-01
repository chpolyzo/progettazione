
def input_numero_positivo(messaggio):
    numero = 0
    is_numero_inserito = False  # variabile sentinella: serve per gestire l'uscita dal ciclo while
    while not is_numero_inserito:
        stringa_inserita = input(messaggio)  # la funzione input restituisce una stringa
        try:  # nel blocco "try" posso eseguire istruzioni che generano errori (eccezioni);
            # nel caso venga generato un errore, il programma non termina ma si esegue il blocco "except"
            numero = float(stringa_inserita)  # questa funzione può generare un errore nella trasformazione da stringa a float
            if numero > 0:
                is_numero_inserito = True
            else:
                print("Il numero inserito è negativo, riprova")
        except Exception:
            print("La stringa inserita non è un numero, riprova")
    return numero


def calcola_tassa(misura1, misura2):
    COSTANTE_TASSA = 9.3 # questa la useremo come costante
    tassa = misura1 * misura2 * COSTANTE_TASSA
    return tassa


def stampa_tassa(tassa):
    # attenzione: tassa è un numero, per poterlo concatenare bisogna convertirlo in stringa
    tassa_stringa = str(tassa)
    print("La tassa da pagare è: " + tassa_stringa)


altezza = input_numero_positivo("Inserisci altezza: ")
larghezza = input_numero_positivo("Inserisci larghezza: ")
tassa = calcola_tassa(altezza, larghezza)
stampa_tassa(tassa)
