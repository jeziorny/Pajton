# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
import math  # ha!

vacation_money = int(input("Ile złotówek zabierasz na wakacje?"))

eur = 4.8
usd = 4.4

pln_to_eur = math.floor(vacation_money // eur)
pln_to_usd = math.floor(vacation_money // usd)

print("Na wakacjach będziesz mieć " + str(pln_to_eur) + " euro, albo " + str(pln_to_usd) + " dolarów.")