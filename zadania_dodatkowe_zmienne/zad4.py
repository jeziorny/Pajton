# Zadanie 4
# Napisz skrypt, który zapyta użytkownika o trzy liczby całkowite,
# a następnie pomnóż dwa pierwsze. przed podzieleniem wyniku przez trzecią liczbę. 
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

first_num = int(input("Podaj liczbę całkowitą, którą nazwiemy 'a':"))
second_num = int(input("Podaj kolejną liczbę całkowit, którą nazwiemy 'b':"))
third_num = int(input("Podaj ostatnią liczbę całkowitą, którą nazwiemy 'c':"))

result = round((first_num * second_num) / third_num, 2)

print("Wynik działania '(a * b) / c' jest równy: " + str(result))

