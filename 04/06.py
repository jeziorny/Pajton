# Napisz grę - kamień (k) / papier (p) / nożyce (n).

# 1. Użytkownik podaje jedną z 3 figur.
# 2. Komputer losuje jedną z 3 figur.
# 3. Sprawdź kto wygrał tę rundę.
# 4. Zmień kod tak, by użytkownik mógł podac liczbę rund.
# 5. Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# 6. Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

MOVES = ["k", "p", "n"]

rounds = ""

while not rounds.isdigit():
    rounds = input("Podaj liczbę rund (wpisz cyfrę): ")

rounds = int(rounds)

while rounds > 0:

    user_choice = ""

    while user_choice not in MOVES and user_choice != "koniec":
        user_choice = input("Wybierz jedną z opcji: k / p / n").lower()

    npc_choice = random.choice(MOVES)

    if user_choice == npc_choice:
        print("Mamy remis!")
    elif user_choice == "k" and npc_choice == "n":
        print("Win!")
    elif user_choice == "n" and npc_choice == "p":
        print("Win!")
    elif user_choice == "p" and npc_choice == "k":
        print("Win!")
    elif user_choice == "koniec":
        print("TCHORZ!")
        break
    else:
        print("CPU wins!")
    
    rounds -= 1
