# 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach. Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)

subjects = ['ala', 'ma', 'kota', 'kota', 'psa', 'psa', 'psa']

""" while len(subjects) < 20:
    user_subjects = input("Podaj cztery przedmioty szkolne (oddzielone spacją): ").lower()
    user_subjects = user_subjects.replace(",", "")
    user_subjects = list(user_subjects.split())
    subjects.extend(user_subjects) """

print(subjects)
counter = 1
most_freq_sub = ""
non_uniques = []

for each in subjects:
    if subjects.count(each) > 1 and each not in non_uniques:
        non_uniques.append(each)
    elif subjects.count(each) > counter:
        counter = subjects.count(each)
        most_freq_sub = each

print(f"Przedmiot '{most_freq_sub}', występuje {counter} razy.")
print(f"Więcej niż raz występują: {non_uniques}")
