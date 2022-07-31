# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy (jest to prawdopodobne)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

fridge_height = int(input("Podaj wysokość lodówki (cm): "))
fridge_width = int(input("Podaj szerokość lodówki (cm): "))
fridge_depth = int(input("Podaj głębokość lodówki (cm): "))

fridge_volume = fridge_height * fridge_width * fridge_depth
fridge_field =  fridge_depth * fridge_width

elevator_height = fridge_height * 1.5
elevator_width = fridge_width * 1.5
elevator_depth = fridge_depth * 1.5

elevator_volume = elevator_depth * elevator_height * elevator_width
elevator_field = elevator_depth * elevator_width

free_volume = elevator_volume - fridge_volume
free_field = elevator_field - fridge_field

print('Po wniesieniu lodówki do windy, zostanie jeszcze '+ str(free_field) + ' cm2. Wolna objętość to: ' + str(free_volume) + ' cm3.')
