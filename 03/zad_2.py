# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

user_num_1 = int(input("Podaj liczbę: "))
user_num_2 = int(input("Podaj drugą liczbę: "))

if user_num_1 + user_num_2 > 100:
    print(user_num_1 + user_num_2)
