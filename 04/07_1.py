# poproś usera o 3 cyfry i wyświetl największą z nich jako wynik

temp_max = -10

for i in range(3):
    usr_num = int(input("Podaj liczbę od 1 do 100: "))
    if usr_num > temp_max:
        temp_max = usr_num

print(f'Największa podana przez usera liczba to {temp_max}')
