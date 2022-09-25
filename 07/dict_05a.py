""" W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

"Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"

Zadbaj o sposób wyświetlania np.:

szybko : 5

zbudź : 1 """

txt = "Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce"
txt = txt.lower().replace(",", "").split()

txt_dict = {}

for word in txt:
    if word in txt_dict:
        txt_dict[word] += 1
    else:
        txt_dict[word] = 1

for key, value in txt_dict.items():
    print(f"{key}: {value}")