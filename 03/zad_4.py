# Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

user_input = input("Podaj ciąg dowolnych znaków: ")

if len(user_input) > 5 and "a" in user_input:
    user_input = user_input.replace("a", "z")
    print(user_input)