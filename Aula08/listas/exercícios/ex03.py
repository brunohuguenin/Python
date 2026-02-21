# Percorra uma lista e encontre o maior número sem usar max().

num = [20,32,101,4,9,78,55,13,7,1,97,93,44,62,89,17,22]

maior = 0

for i in num:
  if i > maior:
    maior = i

print(f"A lista completa: {num}")
print(f"O mauir valor dessa lista é o: {maior}")