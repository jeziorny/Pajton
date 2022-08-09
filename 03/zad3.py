# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

review_user1 = int(input("Oceń ksiązke (1-10): "))
review_user2 = int(input("Oceń ksiązke (1-10): "))
review_user3 = int(input("Oceń ksiązke (1-10): "))

avr_review = (review_user1 + review_user2 + review_user3) / 3

if avr_review > 7:
    print("Bardzo dobra ksiązka")
elif avr_review > 4:
    print("Przeciętna ta ksiązka")
else:
    print("Nie czytaj tego, nie warto")

