""" Wisielec:
Program, będący implementacją gry "wisielec".

Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło. """

secret_pass = "anakonda"
rounds = 10

pass_as_list = list(secret_pass)
masked_pass = len(secret_pass) * ["*"]
used_letters = []

while rounds > 0:
    print(f"Rundy do końca: {rounds}")
    rounds -= 1

    while True:
        user_input = input("Podaj literkę albo wpisz całe hasło: ").lower()

        if len(user_input) == 1 and (user_input in used_letters):
            print("Już podawałeś tę literę.")
            continue
        else:
            break

    used_letters.append(user_input)

    if len(user_input) > 1:
        if user_input == secret_pass:
            print(f"Udało się! Hasło to {secret_pass}")
            break
        else:
            print("Nie udało Ci się :/")
            continue

    if user_input in pass_as_list:
        for index, value in enumerate(pass_as_list):
            if user_input == value:
                masked_pass[index] = user_input
        print("Trafienie!", masked_pass)
    else:
        print("Pudło", masked_pass)
    
    if masked_pass == pass_as_list:
        print(f"Hurra, udało Ci się odgadnąć hasłow: {secret_pass}")
        break
    elif rounds == 0:
        print(f"Nie udało Ci się. Hasło to {secret_pass}")

""" if rounds == 0 and masked_pass != pass_as_list:
    print(f"Nie udało Ci się. Hasło to {secret_pass}") """


