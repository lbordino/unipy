def hide_word(string_word):
    a = ""
    for i in string_word:
        if i != " ":
            a += "_"
        else:
            a += " "
    return a


def game():
    word = input("Inserisci la parola o frase:").lower()
    hidden_word = hide_word(word)
    list_of_char = list(word)
    print("Benvenuto!!", "\n\n")
    print(hidden_word)
    while "".join(list_of_char).replace(" ", "") != "":
        printed_word = ""
        guessed_char = input("\n Scegli la lettera: ").lower()
        if guessed_char in word:
            while guessed_char in list_of_char:
                printed_word = ""
                position_of_char = word.find(guessed_char)
                for i in range(0, position_of_char):
                    printed_word += hidden_word[i]
                printed_word += word[position_of_char]
                if len(printed_word) < len(word):
                    for i in range(position_of_char + 1, len(word)):
                        printed_word += hidden_word[i]
                hidden_word = printed_word
                word = word[:position_of_char] + "-" + word[position_of_char + 1:]
                list_of_char[position_of_char] = ""
            print(printed_word)
        else:
            print("Il carattere non è presente nella parola \n\n")


game()
