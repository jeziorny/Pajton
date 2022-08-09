# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

user_num_1 = int(input("Podaj pierwszą liczbę: "))
user_num_2 = int(input("Podaj drugą liczbę: "))
user_num_3 = int(input("Podaj trzecią liczbę: "))

usr_num_list = [user_num_1, user_num_2, user_num_3]
usr_num_list.sort(reverse=True)

print(usr_num_list)
