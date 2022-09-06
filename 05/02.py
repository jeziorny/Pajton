# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

print("Podaj 10 liczb (użyj cyfr)!")
user_nums = []
COUNTER = 10

while COUNTER > 0:

    user_num = input(f"Wpisz swoją cyfrę (jeszcze {COUNTER}): ")

    while not user_num.isdigit():
        user_num = input("Koniecznie użyj cyfry! Podaj liczbę: ")
    
    user_num = int(user_num)
    user_nums.append(user_num)
    COUNTER -= 1

for num in user_nums:
    if num % 2 == 0:
        print(num)
        