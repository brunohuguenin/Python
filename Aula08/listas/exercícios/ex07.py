# Crie uma nova lista com os elementos de outra lista em ordem inversa sem usar reverse() ou slicing.

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

n_ordem_inversa = []

for i in range(len(numeros), 0, -1):
  n_ordem_inversa.append(i)

print(n_ordem_inversa)