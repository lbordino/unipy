lista =input("Scrivi tre numeri: ").replace(" ", "")
print(lista)
while len(lista) != 3:
    print(lista,"la liste deve essere di 3")
    lista = input("Scrivi tre numeri: ").replace(" ", "")

if lista[0] < lista[1] < lista[2]:
    print("crescente")
elif lista[0] > lista[1] > lista[2]:
    print("Decrescente")
else:
    print("nnulla")
      
    
