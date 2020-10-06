def get_input():
    choice = input("Scegli di forma geometrica vuoi ottenere perimetro e area ").lower().replace(" ", "")
    if choice == "rettangolo":
        dim = input("Definisci base e altezza, nel seguente formato 2,3").split(",")
    elif choice == "triangolo":
        dim = input("Definisci i tre lati, nel seguente formato 1,2,3").split(",")
    elif choice == "quadrato":
        dim = input("Definisci lato, nel seguente formato 2")
    else:
        get_input()
    return dim


def data(list_el):
    try:
        results = []
        perimeter_int = 0
        area = 0
        for i in list_el:
            perimeter_int += list_el[i]
        results.append(perimeter_int)
        if list_el.len == 3:
            s = perimeter_int / 2
            area = (s * (s - list_el[0]) * (s - list_el[1]) * (s - list_el[2])) ** 0.5
        elif list_el.len == 2:
            area = list_el[0] * list_el[1]
        elif len_list == 1:
            area = list_el[0] ** 2
        results.append(area)
        return results
    finally:
        print("Non hai inserito correttamente i valori, riprova")
        get_input()


data(get_input())
