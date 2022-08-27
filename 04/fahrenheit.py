# 1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

# C = 5/9 * (F - 32) - wzór Celsjusz → Fahrenheit

f = 0

# while f < 201:
#     celc = round((5 / 9) * (f - 32), 2)
#     print(f"Fahrenheit : {f} st. -> Celsjusz : {celc}")
#     f += 20

for f in range(0, 201, 20):
    celc = round((5 / 9) * (f - 32), 2)
    print(f"Fahrenheit : {f} st. -> Celsjusz : {celc}")