""" Kółko i krzyżyk:
Program będący implementacją gry w "kółko i krzyżyk" dla dwóch graczy. Wpisz w google "tic tac toe game" i zagraj z google.

Zacznij od zaprojektowania rozgrywki
Możliwość nazwania graczy inaczej niż X / O
Rozszerzeniem gry będzie zmiana 2 gracza na komputer.
Konieczność użycia modułu random. """

# sama mechanika, bez planszy

plansza = [
  ['-', '-', '-'],
  ['-', '-', '-'],
  ['-', '-', '-']
]

empty_spots = 0

for row in plansza:
    empty_spots = 0
    for each in row:
        if each == '-':
            empty_spots += 1

print(empty_spots)

while empty_spots > 0:



    for row in plansza:
        print(row)

    player_X_row = int(input("W którym rzędzie chcesz wstawić krzyżyk? (cyfra: 1, 2, 3): "))
    player_X_col = int(input("Na którym miejscu w rzędzie? (cyfra: 1, 2, 3): "))

    player_X_row -= 1
    player_X_col -= 1

    plansza[player_X_row][player_X_col] = "X"
    empty_spots -= 1

    for row in plansza:
        print(row)

# plansza[0][1] = " X "
