# Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

exl_set = set(example_list)
exl_tup = tuple(exl_set)

print(max(exl_tup), min(exl_tup))