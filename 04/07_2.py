# ▹ Stwórz grę ciepło zimno.

# 1. Komputer losuje liczbę z zakresu od 1 do 100.
# 2. Użytkownik podaje swój traf.
# 3. Komputer odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# 4. Jeśli użytkownik zgadnie wygrywa gracz.
# 5. Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

cpu_num = random.randint(1, 101)
cpu_user_diff = 100

for _ in range(6):
    
    user_num = input("Wpisz cyfrę z zakresu 1-100: ")

    while not user_num.isdigit():
        user_num = input("Musisz podać CYFRĘ (wyrażoną cyfrą arabską) z zakresu 1-100: ")
    user_num = int(user_num)

    while user_num <= 0 or user_num > 100:
        user_num = int(input("Cyfra MUSI być z zakresu między 1 a 100: "))
    
    cur_distance = abs(cpu_num - user_num)

    if user_num == cpu_num:
        print(f"Wygrałeś! Właściwa liczba to {cpu_num}!")
        break
    elif cur_distance < cpu_user_diff:
        print("Ciepło!")
        cpu_user_diff = cur_distance
    elif cur_distance == cpu_user_diff:
        print("Bez zmian!")
    else:
        print("Zimno!")
        

if user_num != cpu_num:
    print(f"Komputer wygrał! Właściwa liczba to {cpu_num}!")
