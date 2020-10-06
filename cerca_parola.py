def cerca_parola_bool():
    find_word = input("Parola da cercare: ") in input("Frase in cui cercarla: ")
    return find_word


print(cerca_parola_bool())


def cerca_parola_string():
    find_word = input("Parola da cercare: ")
    found_word = input("Frase in cui cercarla: ")
    int_word = found_word.find(find_word)
    return found_word[int_word:len(find_word):+1]

# print(fast_search())
