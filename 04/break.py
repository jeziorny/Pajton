for val in "string":
    if val == "i":
        break
    print(val)

print("Koniec")

# continue po trafieniu warunku przerywa kod i wykonuje od następnego elementu

for val in "string":
    if val == "i":
        print("LALA")
        continue
    print(val)

print("Koniec")