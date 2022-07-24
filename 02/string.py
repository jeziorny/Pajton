from urllib.parse import quote_plus


txt = "Lubię kaszankę"
word = "python"

# print(txt[0], txt[1], txt[2])
# print(txt[0:5])

print(word[:3], word[3:])

print(txt[::2])

print("Pi" + word[2:])

word = word.replace("y", "i")
print(word)

# Jak sprawdzić czy ciąg znaków składa się tylko z cyfr?
tel_no = "1234"
print(tel_no.isdigit())

# Jak wyświetlić wyśrodkowany tekst o zadanej szerokości i dodatkowo puste miejsca wypełnić np. gwiazdką: '***mata***'

text = "helou"
text = text.center(20, "*")
print(text)

# Jaka metoda usunie znaki tylko z prawej strony?
address = "www.doMena"
address = address.lstrip("w.")
print(address)

# Jak sprawdzić czy ciąg ma co najmniej jedną dużą literę?
print(not address.isupper() and not address.islower() and address.isalpha())

# Policz ile razy zadany ciąg znaków np. ('na') wystąpił w ciągu znaków ('banana' = 2)
banana = "banana"
print(banana.count("na"))

# 1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

long_text = "Hejo wariaty!"
mid_index = len(long_text) // 2
print(long_text[mid_index-1:mid_index+2])

# 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = "Hello "
s2 = "World!"
s3 = s1.removesuffix("lo ") + s2 + s1.removeprefix("Hel")
print(s3)

# 3. Do zmiennej quote przypisz zdanie: Wyświetl cały cytat odwrotnie

quote = "Honesty is the first chapter in the book of wisdom."
print(quote[::-1])

# Policz wszystkie znaki w napisie
print(len(quote))

# Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[51-7:-1])

# Wyświetl tylko pierwszą połowę tekstu
print(len(quote) // 2)
print(quote[:25])

# Wyświetl tylko kropkę
print(quote[-1])

# Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[len(quote) // 2::3])

# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print("Hnsyi h is hpe ntebo fwso.") # :D
print(quote[::2])

# Zamień wisdom na słowo friendship
print(quote[:-7] + "friendship.")

