SOGLIA_SINGLE = 32000
SOGLIA_SPOSATO = 64000
RATE_SOTTO_SOGLIA = 0.10
RATE_SOPRA_SOGLIA = 0.25
tax = 0.0
stato = input("Hai famiglia a carico Y/N?: ")
reddito = float(input("Inserisci reddito:"))
if stato.upper() == "Y": #l'upper fa sì che la y risulti maiuscola
    if reddito <= SOGLIA_SPOSATO:
        tax = reddito*RATE_SOTTO_SOGLIA
    else:
        tax = SOGLIA_SPOSATO*RATE_SOTTO_SOGLIA + (reddito-SOGLIA_SPOSATO)*RATE_SOPRA_SOGLIA
elif stato.upper() == "N":
    if reddito <= SOGLIA_SINGLE:
         tax = reddito*RATE_SOTTO_SOGLIA
    else:
         tax = SOGLIA_SINGLE*RATE_SOTTO_SOGLIA + (reddito-SOGLIA_SINGLE)*RATE_SOPRA_SOGLIA
else:
    print('Stato non valido')
print('Ammontare tasse: ', tax)
