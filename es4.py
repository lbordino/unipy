NUM_LIB = 100
COST = 1000

def prezzo(costo, num):
    costo = 0.075 * costo + costo
    costo += num * 2
    return costo

print(prezzo(100, 3))

