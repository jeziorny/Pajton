# Zadanie 3

print("------------------ Sumowanie liczb ------------------")
print("Program pyta użytkownika o 4 dowolne liczby całkowite")
print("a następnie zwraca ich sumę.")
print()

first_num = int(input("Podaj liczbę całkowitą: "))
second_num = int(input("Podaj kolejną liczbę całkowitą: "))
third_num = int(input("I jeszcze kolejną liczbę całkowitą: "))
fourth_num = int(input("I juz ostatnią liczbę całkowitą: "))

sum_nums = first_num + second_num + third_num + fourth_num

print("Suma podanych przez Ciebie liczb to: " + str(sum_nums))
