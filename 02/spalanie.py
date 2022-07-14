# spalanie

# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

spalanie = float(input("Podaj spalanie Twojego auta: "))
dystans = float(input("Jaki dystans chcesz przejechać (w km): "))
cena_paliwa = float(input("Jaka jest cena paliwa za litr: "))

spalone_paliwo = spalanie * (dystans / 100)

suma = spalone_paliwo * cena_paliwa

print(round(suma, 2))