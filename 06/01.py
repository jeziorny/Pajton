# Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę krotkę na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.

pet = ("dog", "husky", "Wutang")

race, breed, name = pet

print(f"My {race} is a {breed} named {name}.")

