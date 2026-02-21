# Dada uma lista de números, substitua todos os valores negativos por 0.

num = [2, -1, 2, 6, 14, -75, -17, 63, 87, 0, 100, 14,-101]

print(f"A lista original: {num}")
num_negativo = []

for i, valor in enumerate(num):
  if valor < 0:
    num_negativo.append(valor)
    num[i] = 0 

print(f"Os valores negativos: {num_negativo}")
print(f"A lista oiginal sem os valores negativos: {num}")