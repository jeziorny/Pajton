# subject = input("Podaj przedmiot szkolny: ")
# grade = input("Ocena w skali 1-6: ")

# print(subject, " : ", grade)
subjects = []
grades = []

for i in range(3):
    subject = input("Podaj przedmiot szkolny: ")
    subjects.append(subject)
    grade = input("Ocena w skali 1-6: ")
    grades.append(grade)

l = len(subjects)

while l > 0:
    print(subjects[l - 1], " : ", grades[l - 1])
    l = l - 1
