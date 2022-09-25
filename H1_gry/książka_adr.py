""" Książka adresowa:
Program przechowujący danę kontaktowe znajomych/klientów.

Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. 

Zadania to:

Wyświetlenie wszystkich wpisów
Stworzenie nowego wpisu (dane wczytywane z klawiatury)
Usunięcie wpisu
Zakończenie pracy programu
Program powinien na starcie mieć już wprowadzone kilka wpisów. """

adress_book = {
    "1":  {
        "name": "Jan",
        "last": "Smith",
        "phone": "64246457"
    },
    "2":  {
        "name": "Adam",
        "last": "Clark",
        "phone": "05332183"
    },
    "3": {
        "name": "Sarah",
        "last": "Connor",
        "phone": "92745693"
    }
    
}

start = input("Chcesz wejść w KONTAKTY (t/n): ")

while start == "t":

    print("Dostępne opcje: \n 1. Zobacz wszystkie \n 2. Stwórz nowy \n 3. Usuń kontakt \n 4. Zakończ")

    user_choice = input("Podaj numer polecenia (np. '1'): ")

    if user_choice == "1":

        print("Wszystkie Twoje kontakty: ")
        for uuid, val in adress_book.items():
            print("Kontakt:", val["name"], val["last"], " Tel.:", val["phone"])
    elif user_choice == "2":

        name = input("Podaj IMIE kontaktu: ").lower()
        last = input("Podaj NAZWISKO kontaktu: ").lower()
        phone = input("Podaj NUMER TELEFONU kontaktu: ")

        ks = adress_book.keys()
        ks = list(ks)
        new_key = ks[-1]

        adress_book[str(int(new_key) + 1)] = name, last, phone
        print(adress_book)

    elif user_choice == "3":

        print("Kontakty: ")

        for uuid, val in adress_book.items():
            print(uuid, val["name"], val["last"], " Tel.:", val["phone"])

        user_del = input("Wpisz NUMER kontaktu, który chcesz usunąć (cyfrą): ")
        adress_book.pop(user_del)

    elif user_choice == "4":
        print("Bye!")
        break
        


