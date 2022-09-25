""" W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

"Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"

Zadbaj o sposób wyświetlania np.:

szybko : 5

zbudź : 1 """

txt = "Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce"
txt = txt.lower().replace(",", "").split()
# txt = txt.replace(",", "")
# txt = txt.split()

lex = set(txt)

for word in lex:
    print(word, ":", txt.count(word))
    
        