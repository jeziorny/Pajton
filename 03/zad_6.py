# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!

import random

user_number = int(input("Podaj liczbę w zakresie 1 do 100: "))
dev_number = int(random.randrange(1, 100, 1))

if user_number == dev_number:
    print("Gratulacje! Udało Ci się trafić liczbę programisty!")
else:
    print(f"Niestety, nie udało Ci się. Poprawna liczba to: {dev_number} :/")
