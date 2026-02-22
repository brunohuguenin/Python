# Crie uma nova tupla com os elementos da tupla original em ordem inversa
# (sem usar slicing ou `reversed()`)

tupla_original = ("uva", "maçã", "pêra", "acerola", "manga", "limão")
print(f"Tupla original: {tupla_original}")

tupla_transformada = list(tupla_original)
lista_inversa = []

for i in range(len(tupla_transformada) -1, -1, -1):
  lista_inversa.append(tupla_transformada[i])

tupla_inversa = tuple(lista_inversa)
print(f"Tupla com os valores inverso da original: {tupla_inversa}")
