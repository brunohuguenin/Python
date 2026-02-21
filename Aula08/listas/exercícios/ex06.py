# Dada uma lista de números, remova todos os números pares usando for (cuidado com a iteração).

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

numeros_impares = [n for n in numeros if n % 2 != 0]

print(f"Lista original: {numeros}")
print(f"Lista sem os números pares{numeros_impares}")
