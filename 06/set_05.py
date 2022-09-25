# Porównaj zachowanie discard() vs remove() dla typu set.

s = {1, 4, 6, "a"}
print(s)

# Usuwa element ze zbioru jeśli ten się zawiera. Jeśli nie - nic nie robi
s.discard(4)

print(s)

# Usuwa element ze zbioru jeśli ten się zawiera. Jeśli nie - zwraca błąd
s.remove("b") 