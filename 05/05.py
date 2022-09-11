""" Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

Dorota, Wellman, dziennikarka

Adam, Małysz, sportowiec

Robert, Lewandowski, piłkarz

Krystyna, Janda, aktorka

Wyświetl w sposób przyjazny dla użytkownika """

peuple = [["Dorota", "Wellman", "dziennikarka"], ["Adam", "Małysz", "sportowiec"], ["Robert", "Lewandowski", "piłkarz"], ["Krystyna", "Janda", "aktorka"]]

for row in peuple:
    # print(f"{row[0]} {row[1]}, {row[2]}")
    for col in row:
        if col != row[-1]:
            print(col, end=" ")
        else:
            print(col, end=".")
    print()