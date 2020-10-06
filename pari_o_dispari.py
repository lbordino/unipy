import random as rd


def side():
    choice = input("Scegli pari o dispari? ").lower().replace(" ", "")
    if choice == "pari":
        return True
    elif choice == "dispari":
        return False
    else:
        side()


def is_even(int1, int2):
    return not bool((int1 + int2) % 2)


def number():
    you = input("Scegli che numero usare ").replace(" ", "")
    if you.isnumeric():
        return int(you)
    else:
        number()


def game():
    print("Bingo Bango Bongo Benvenuto ")
    p_o_d = side()
    y_number = number()
    cpu = rd.randint(1, 200)
    print("Il pc ha scelto:", cpu)
    bool_is_even = is_even(y_number, cpu)
    if (bool_is_even and  p_o_d) or (bool_is_even and not p_o_d):
        print("Hai vinto")
    else:
        print("Hai perso")


game()
