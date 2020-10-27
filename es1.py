V_UNO = input("inserisci il valore 1 :")
V_DUE = input("inserisci il valore 2: ")

def somma(a,b):
    return a + b

def prodotto(a,b):
    return a * b

def v_medio(a,b):
    return (a + b)/2

def dist(a,b):
    return abs(somma(a,b))

print(max(V_UNO,V_DUE))
print(min(V_UNO,V_DUE))
