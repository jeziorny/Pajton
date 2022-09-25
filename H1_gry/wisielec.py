""" Wisielec:
Program, będący implementacją gry "wisielec".

Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło. """


PASSWORD = "anakonda"  # hasło do odgadnięcia
pass_as_list = list(PASSWORD)  # zmieniam w listę żeby było mutowalnie
obfuscated_password = []  # do wyświetlania userowi + stan hasła
users_picks = []  # przechowuję litery podane przez usera w grze
ROUNDS = 10
guessed_pass = False

# tworzę zobfuskowane hasło do wyświetlania userowi
for letter in PASSWORD:
    obfuscated_password.append("*")

while ROUNDS > 0:
    # pobieram od usera literę
    print(f"Hasło ma {len(PASSWORD)} znaków: ", "".join(obfuscated_password))
    USER_GUESS = input(f"Podaj literę (masz {ROUNDS} prób) lub wpisz 'TRY': ").lower()
    
    while USER_GUESS == "try":
        user_try = input("Odgadnij hasło: ")
        if user_try == PASSWORD:
            print("BRAWO! Udało Ci się! Hasło to:", PASSWORD)
            guessed_pass = True
        else:
            USER_GUESS = input("Niestety, to nie jest hasło. Podaj literę:").lower()
    if guessed_pass:
        break

    # Sprawdzam czy user podał literę alfabetu
    while not USER_GUESS.isalpha():
        USER_GUESS = input("Podaj jedną LITERĘ: ").lower()
    # Sprawdzam czy user nie podał głoski dwuliterowej, jak "cz"
    while len(USER_GUESS) > 1:
        USER_GUESS = input("Podaj JEDNA literę: ").lower()
    # Sprawdzam czy user nie podał już tej litery
    while USER_GUESS in users_picks:
        USER_GUESS = input("Podawałeś już tę literę. Podaj inną: ").lower()

    # Jeśli litera z hasła = literze usera to zastępuję indeksowany znak w OBF...
    for index, letter in enumerate(pass_as_list):
        if letter == USER_GUESS:
            obfuscated_password[index] = letter

    # Sprawdzam czy hasło nie zostało już odkryte przez sprawdzenie str OBF.. z PSW
    if "".join(obfuscated_password) == PASSWORD:
        print("Gratulacje, udało Ci się odgadnąć hasło:", "".join(obfuscated_password))
        break

    ROUNDS -= 1

# Jeśli rundy się skończyły to user przegrywa
if ROUNDS == 0:
    print("Niestety, nie udało Ci się. Hasło to:", PASSWORD)
