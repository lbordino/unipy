def calc():
    print(
        "calcolatrice in esecuzione \n digita 1 per addizione \n digita 2 per sottrazione \n digita 3 per moltiplicazione \n digita 4 per divisione \n digita 5 per esponente \n esc per uscire ")
    scelta = input('inserisci numero --> ')
    if scelta == '1':
        print("addizione")
        a = float(input('numero 1 --> '))
        b = float(input('numero 2 --> '))
        print("risultato : ", a + b)

    elif scelta == '2':
        print("sottrazione")
        a = float(input('numero 1 --> '))
        b = float(input('numero 2 --> '))
        print("risultato : ", a - b)

    elif scelta == '3':
        print("moltiplicazione")
        a = float(input('numero 1 --> '))
        b = float(input('numero 2 --> '))
        print("risultato : ", a * b)

    elif scelta == '4':
        print("divisione")
        a = float(input('numero 1 --> '))
        b = float(input('numero 2 --> '))
        print("risultato : ", a / b)

    elif scelta == '5':
        print("esponente")
        a = float(input('numero 1 --> '))
        b = float(input('numero 2 --> '))
        print("risultato : ", a ** b)

    elif scelta == 'esc':
        print("chiusura")

    loop = input('continuare? SI/NO ').lower()
    print(loop)
    if loop == "si":
        print(" menù principale ")
        calc()
    else:
        print(" stop")


calc()
