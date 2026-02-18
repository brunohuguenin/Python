# Encontre o maior número de uma tupla sem usar max().

val = (1, 5, 10, 5, 20, 15, 25, 20, 5, 30, 35, 5, 40, 45, 50, 55, 60, 5, 70, 5)

maior = 0

for i in val:
  if maior < i:
    maior = i

print(f"Tulpa completa {val}")
print(f"Maior valor da tupla: {maior}")