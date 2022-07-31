# Zadanie 8
# Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.
import math

vacation_money = int(input("Ile złotówek zabierasz na wakacje?"))

eur = 4.8

pln_to_eur = math.floor(vacation_money // eur)

fifties = pln_to_eur // 50
pln_to_eur = pln_to_eur - (fifties * 50)  # aktualizacja wartości EUR

twenties = pln_to_eur // 20
pln_to_eur = pln_to_eur - (twenties * 20)  # aktualizacja wartości EUR

tens = pln_to_eur // 10
pln_to_eur = pln_to_eur - (tens * 10)  # aktualizacja wartości EUR

fives = pln_to_eur // 5
pln_to_eur = pln_to_eur - (fives * 5)  # aktualizacja wartości EUR

ones = pln_to_eur

print("Dostaniesz swoje euro w następujących nominałach: 50 EUR = " + str(fifties) + ", 20 EUR = " + str(twenties) + ", 10 EUR = " + str(tens) + ", 5 EUR = " + str(fives) + ", 1 EUR = " + str(ones))