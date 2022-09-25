""" Generator imienia dla Wojownika RPG:
Konieczność użycia modułu random.
Program generuje wymawialne(!) imię o zadanej długości i dodaje do niego przydomek (opcjonalnie również tytuł i liczebnik). Np. 'Jouxdrien II Niemrawy'.
Pomysł jest zainspirowany grą: http://progressquest.com/play/main.html
Imię musi zaczynać się od wielkiej litery.
Program można kontynuować używając pomysłu poniżej. """

import random

# Sets/lists for the generator
consonants = ["b", "c", "d", "k", "s", "t", "w", "z", "m", "n", "j", "k", "v", "p", "x", "z", "g", "f"]
vowels = ["a", "e", "i", "o", "u"]
of_num = ["IX", "I", "IV", "V", "II", "III", "IV", "I", "II", "III", ]
by_name = ["Bebzol", "Sałatka", "ze Smarków", "Mądrala", "Myszka", "Rabarbar", "Kijanka", "z Księżyca"]

# Var to hold name + name length gen
name = ""
no_of_syls = random.randrange(2, 5)

# Name generator
for i in range(no_of_syls):
    random_cons = consonants[random.randrange(len(consonants))]
    random_vow = vowels[random.randrange(len(vowels))]
    name += random_cons
    name += random_vow

name = name.capitalize()
name += " " + of_num[random.randrange(len(of_num))]
name += " " + by_name[random.randrange(len(by_name))]

print(name)
