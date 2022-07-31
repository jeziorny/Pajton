# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 

first_num = int(input("Podaj liczbę całkowitą, którą nazwiemy 'a':"))
second_num = int(input("Podaj kolejną liczbę całkowit, którą nazwiemy 'b':"))

res_division = round(first_num / second_num, 2)
res_modulo = round(first_num % second_num, 2)

print(f"Wynik dzielenia to: " + str(res_division) + " .A reszta z tego dzielenia to: " + str(res_modulo))