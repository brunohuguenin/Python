# Percorra uma lista e gere duas novas listas: uma com números pares e outra com ímpares.

import random

numeros = [random.randint(1, 100) for _ in range(20)]

numeros_pares = [n for n in numeros if n % 2 == 0]
numeros_impares = [n for n in numeros if n % 2 != 0]


print(f"Lista original: {numeros}")
print(f"Lista com os números pares: {numeros_pares}")
print(f"Lista com os números ímpares: {numeros_impares}")