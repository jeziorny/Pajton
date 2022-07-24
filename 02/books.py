# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

book_title = input("Podaj tytuł ksiązki: ")
book_author = input("Wpisz autora tej ksiazki: ")
book_pages = input("Ile stron ma ksiazka?")

# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.

print(book_title.isalpha())
print(book_author.isalpha())
print(book_pages.isnumeric())

# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
book_title = book_title.capitalize() # W PL tylko tytuł będzie z wielkiej. Przy US/EN wolałbym .title() zeby kazde słowo było z wielkiej.
book_author = book_author.title()

# Połącz dane w jeden ciąg book za pomocą spacji
book = book_author + " " + book_title + " " + book_pages
print(book)

# Policz liczbę wszystkich znaków w napisie book
print(len(book))
