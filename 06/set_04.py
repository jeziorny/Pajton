# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

long = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

for i in range(0, len(long), 4):
    sublist = long[i:i+4]
    # sublist = sublist.reverse()
    print(sublist)
