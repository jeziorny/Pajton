# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

# palindrom = input("Wpisz zdanie, które jest palindromem: ") < Tego bym uzył zeby zebrać input
palindrom = "Kobyła ma mały bok." # dla wygody przyjąłem stałą wartość pseudo-inputa

palindrom = palindrom.strip(" .,!?") # usuwam spacje i znaki sprzed i zza palindromu
palindrom = palindrom.replace(" ", "") # zastępuję wszystkie spacje niczym

pali_check = palindrom[::-1].lower() # string z odwróconem palindromem, tylko w niskich znakach

print(palindrom.lower() == pali_check.strip(" ."))
