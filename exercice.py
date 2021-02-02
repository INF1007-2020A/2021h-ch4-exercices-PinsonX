#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string) % 2 == 0:
        return True


def remove_third_char(string: str) -> str:
    return string[:2] + string[3:]


def replace_char(string: str, old_char: str, new_char: str) -> str:

    new_string = string
    displace = -(len(new_char) - 1)
    L = len(old_char)
    x = -1
    for char in string:
        x += 1
        if string[x:x + L] == old_char:
            displace += len(new_char) - 1
            new_string = new_string[:x + displace] + new_char + new_string[x + displace + L:]

    return new_string


def get_number_of_char(string: str, char: str) -> int:
    x = 0
    for chr in string:
        if chr == char:
            x += 1
    return x


def get_number_of_words(sentence: str, word: str) -> int:

    x = -1
    nb = 0
    for char in sentence:
        x += 1
        if sentence[x:x + len(word)] == word:
            nb += 1
    return nb

def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    chaine = "hello"
    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
