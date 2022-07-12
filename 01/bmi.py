# BMI

h = float(input("Podaj wzrost w metrach z kropeczką: "))
w = float(input("Podaj wagę w kg:"))

bmi = round(w / (h ** 2), 2)


print("Twoje BMI to: " + str(bmi))