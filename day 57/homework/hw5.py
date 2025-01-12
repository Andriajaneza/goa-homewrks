def abbrev_name(name):
    first_word, second_word = (name.split())
    return ((first_word[0].upper()) + (".") + (second_word[0].upper()))
