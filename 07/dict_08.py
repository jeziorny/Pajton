# Utwórz słownik dla 10 (albo 5) krajów Europy zawierajacy listy 10 (albo 4) najpopularniejszych imion żeńskich. Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.

# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

fem_names = {
    "UK": ["Isla", "Emma", "Olivia", "Lily"],
    "Germany": ["Emilia", "Hannah", "Sophie", "Lina"],
    "France": ["Julia", "Louise", "Éléanor", "Charlotte"],
    "Italy": ["Sophie", "Aurora", "Emma", "Julia"],
    "Croatia": ["Mia", "Emma", "Sophie", "Sarah"]
}

names = []

for name in fem_names.values():
    names.extend(name)

for name in names:
    if names.count(name) > 2:
        print(name)
        names.remove(name)

