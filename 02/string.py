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

# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

long_text = "Hejo wariaty!"
mid_index = len(long_text) // 2
print(long_text[mid_index-1:mid_index+2])

# Do zmiennej quote przypisz zdanie: Wyświetl cały cytat odwrotnie

quote = "Honesty is the first chapter in the book of wisdom."
print(quote[::-1])