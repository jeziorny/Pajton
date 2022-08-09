# Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”

user_no = int(input("Podaj liczbę: "))

if user_no % 3 == 0:
    print("Twoja liczba jest podzielna przez 3")