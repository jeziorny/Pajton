# Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

days_list = []

for v in days.values():
    days_list.append(v)

days_list = set(days_list)
days_list = list(days_list)

print(days_list)
