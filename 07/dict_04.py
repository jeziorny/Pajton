# Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.

# [([0]*cols) for i in range(rows)]

multi_tab = []
col = 1

while col <= 10:
    row = []
    for i in range(1, 11):
        row.append(i * col)
    multi_tab.extend([row])
    print(row)
    col += 1

print(multi_tab)