# Dada uma lista de números, conte quantos são pares usando um loop.

num = [20,32,4,9,78,55,13,7,1,97,93,44,62,89,17,22]

lista_pares = []
contagem = 0

for i in num:
  if i % 2 == 0:
    contagem += 1
    lista_pares.append(i)

print(f"A lista completa: {num}")
print(f"Na lista tem {contagem} números pares que são: {lista_pares}")