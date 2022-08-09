# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 małą literę, 1 dużą literę i mieć długość conajmniej 8 znaków. Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input("Podaj hasło: ")

if not len(password) < 8:
    print("Twoje hasło musi mieć min. 8 znaków")

if password.isalpha() or password.isdigit():
    print("Twoje hasło musi się składać z cyfr i liter")

if not password.islower() and not password.isupper():
    print("Twoje hasło MUSI zawierać conajmniej jedną duzą oraz małą literę")

# czy są litery
# czy są cyfry
# czy jest duza litera
# czy jest mała litera
