# W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

txt = "1 asd . KO"  # Instead of taking input I made it a ready made string

low_let = 0
capt_let = 0
nos = 0
spec = 0

for i in txt:
    if i.isnumeric():
        nos += 1
    elif not i.isalnum():  # if not alnum then it must be a spec char rite?
        spec += 1
    elif i.isupper():
        capt_let += 1
    elif i.islower():
        low_let += 1

print(f"Mamy tu {low_let} małych liter i {capt_let} wielkich. Do tego {nos} liczb i {spec} znaków specjalnych.")


# 1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.

names = "Ada, Julia, Java, Ruby"

names_table = names.split(",")

for each in names_table:
    print("Hey" + each)


# 2▹ Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = "abrakadabra"
sliced_txt = ""

for i in range(1, len(txt), 2):
    sliced_txt += txt[i]

print(sliced_txt)
print(txt[1::2])  


# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż zgadnie.

SECRET_NUM = 7

user_num = int(input("Podaj liczbę od 0 do 20, żeby odgadnąć magiczną liczbę: "))

while user_num != SECRET_NUM:
    user_num = int(input("To nie ta. Spróbuj jeszcze raz: "))

print(f'Udało Ci się! Magiczna liczba to {SECRET_NUM}!')

# Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

ingredients = ["makaron", "pomidory", "czerwone wino", "oliwa z oliwek"]

for each in ingredients:
    print(f'Dodaj {each}')

# Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników. Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

s = 0

for i in range(1, 11):
    s += i
    print(s)

# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

user_number = int(input("Podaj liczbę naturalną mniejszą niż 9: "))
fact = 1

if user_number > 8:
    user_number = int(input("Twoja liczba jest większa niż 9. Podaj mniejszą: "))
else:
    for i in range(1, user_number + 1):
        fact = fact * i

print(f"Silnia dla {user_number} to: {fact}")