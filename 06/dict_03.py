# Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

# a = [[0] * cols] * rows

n = 3
tab = [["_"] * n] * n

""" for r in range(n):
    row = []
    for col in range(n):
        row.append("_")
    tab.append(row) """

""" 
    tmp = []
    for i in range(n):
    tmp.append("_")
    tab.append(tmp) """

print(tab)
