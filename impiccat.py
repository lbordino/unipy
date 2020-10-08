parDaIndovinare = "gigi"  # la tua parola scelta per il gioco dell'impiccato

posLetIndovinate = []  # posizioni delle lettere indovinate
stringaUtente = ""  # ciò che scrive l'utente
print("Non dovresti saperlo, ma la parola da indovinare è \"" + parDaIndovinare + "\".")
while stringaUtente != "stop":  # se non scrive "stop", fai:
    stringaUtente = input()  # fagli scrivere qualcosa
    while len(stringaUtente) > 1 or stringaUtente.isnumeric() == True:
        # se scrive più di una lettera, o scrive numeri, non va bene
        # ----------------------------------------
        # | PICCOLA PARENTESI:                   |
        # | a = "2"                              |
        # | print(a.isnumeric())                 |
        # |  -> uscirebbe True,                  |
        # | anche se a è una stringa.            |
        # ----------------------------------------

        print("Inserisci una lettera per volta.")
        stringaUtente = input()  # rifagli scrivere qualcosa in quel caso.
        # se tutto va bene invece:
    stringaUtente = stringaUtente.lower()  # converti tutto in minuscolo
    i = 0  # contatore
    trovata = "no"  # mi serve per capire se quella lettera
    # c'è nella parDaIndovinare.
    while i < len(parDaIndovinare):  # per ogni lettera della parola da indovinare
        # (uso while per cambiare, perchè qui tengo conto di i)
        if stringaUtente == parDaIndovinare[i] and stringaUtente != " ":
            # controlla se la lettera di indice i nella
            # stringaUtente è uguale a quella letDaIndovinare.
            posLetIndovinate.append(i)  # se sì, metti in lista le posizioni
            # dove quella lettera è collocata in parDaIndovinare
            trovata = "si"  # se la trovi, dimmelo, così mi regolo per la risposta.
            # se non la trova resta a "no"
        i = i + 1  # aggiorna il contatore

    if trovata == "si":  # l'ha trovata?
        print("La lettera " + stringaUtente + " si trova nelle posizioni " + str(posLetIndovinate) + ".")
    else:
        print("La lettera " + stringaUtente + " non c'è nella parola da indovinare.")
    posLetIndovinate.clear()  # devo resettare la lista delle posizioni,
    # altrimenti tra una lettera e l'altra mi dice
    # sia le posizioni dove si trova quella attuale,
    # sia le posizioni dove si trovava quella di prima.