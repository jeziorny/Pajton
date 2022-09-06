# ▹ Stwórz grę ciepło zimno.

# 1. Komputer losuje liczbę z zakresu od 1 do 100.
# 2. Użytkownik podaje swój traf.
# 3. Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# 4. Jeśli użytkownik zgadnie wygrywa gracz.
# 5. Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

npc_num = random.randint(1, 101)

temp_distance = 100

rounds = 6

while rounds > 0:
    user_num = int(input("Wybierz cyfrę z zakresu 1-100: "))
    
    if user_num == npc_num:
        print("Udało się!")
        break

    current_distance = abs(npc_num - user_num)

    if current_distance < temp_distance:
        temp_distance = current_distance
        print("Cieplej!")
    elif current_distance == temp_distance:
        print("Bez zmian")
    else:
        print("Zimniej!")

    rounds -= 1

if rounds == 0:
    print(f'Wygrał komputer, dzięki wspaniałej liczbie {npc_num}')