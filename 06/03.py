# Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.

nums = (1, 12, 35, 40, 53, 66)

user_num = int(input("Podaj liczbę całkowitą: "))

if user_num in nums:
    print(nums.index(user_num))

""" for ind, val in enumerate(nums):
    if user_num == val:
        print(ind)
 """

if user_num not in nums:
    print("Nie ma takiej liczby no.")
    