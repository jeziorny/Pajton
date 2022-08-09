# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

# kod z bmi.py:
h = float(input("Podaj wzrost w metrach z kropeczką: "))
w = float(input("Podaj wagę w kg: "))

bmi = round(w / (h ** 2), 2)

print("Twoje BMI to: " + str(bmi))

if bmi < 18.5:
    print("Masz niedowagę!")
elif bmi < 25:
    print("Twoja waga jest normalna")
elif bmi < 30:
    print("Masz nadwagę!")
else:
    print("OTYŁOŚĆ!")