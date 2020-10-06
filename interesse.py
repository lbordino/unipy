def n_month(init_money):
    n_month_int = 0
    while init_money > 0:
        init_money += init_money * 0.005
        init_money -= 500
        n_month_int += 1
    return int(n_month_int / 12)


print(n_month(10000))

# definisco n_month_int come il numero di mesi
#     finchè i soldi sul conto sono più di 0
#         aggiungi l'interesse di 0.5%
#         togli 500 per le spese
#         aggiungi al counter 1 (numero dell'iterazione)
#     returna il valore dei mesi/12 reso intero
