# Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

print("Podaj parzystą liczbę elementów!")
user_arr = []

while len(user_arr) < 2:
    user_element = input("Podaj element: ")
    user_arr.append(user_element)

while len(user_arr) % 2 == 0:
    to_cont = input("Masz już parzystą l. elementów. Wpisz 't' aby dodać kolejne 2 lub cokolwiek aby zakończyć: ")
    if to_cont == "t":
        user_element = input("Podaj element: ")
        user_arr.append(user_element)
        user_element = input("Podaj kolejny element: ")
        user_arr.append(user_element)
    else:
        break

result = user_arr[len(user_arr) // 2 - 1] == user_arr[len(user_arr) // 2]

print("Two middle elements have the same value:", result)
