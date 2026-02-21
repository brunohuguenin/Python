# Percorra um conjunto e conte quantos números são pares.

num = {10,15,20,25,30,35,40,45,50}
contador = 0
for i in num:
  if i % 2 == 0:
    contador += 1

print(f"Conjunto completo: {num}")
print(f"Quantidade de números pares: {contador}")