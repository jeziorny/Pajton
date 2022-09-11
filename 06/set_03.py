# Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

t1 = (1, 2, 3, 4)
t2 = ("a", "b", "c")

l = list(t1[::2] + t2[1::2])

print(l)

l = set(l)
print(l)

""" l.extend(t1[::2])
l.extend(t2[1::2]) """

""" for ind, val in enumerate(t1):
    if ind % 2 == 0:
        l.append(val)

for ind, val in enumerate(t2):
    if ind % 2 != 0:
        l.append(val) """

