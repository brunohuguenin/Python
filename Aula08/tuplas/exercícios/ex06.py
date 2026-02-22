# Dada uma tupla de números, crie uma lista contendo apenas os valores pares.

import random

numeros_tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(f"Tupla original: {numeros_tupla}")

numeros_lista = list(numeros_tupla)
print(f"Lista gerada a partir da tupla: {numeros_lista}")

numeros_pares = [p for p in numeros_lista if p % 2 == 0]
print(f"Lista com os números pares: {numeros_pares}")


