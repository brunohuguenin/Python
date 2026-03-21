# Dictionary Comprehensions

didicionario = {}

for i in range(5):
  didicionario[i] = i * 2
print(didicionario)


# Dictionary Comprehensions com condições
dicionario = {i:i * 2 for i in range(5)}
print(dicionario)

quadrados = {x: x**2 for x in range(5)}
print(quadrados)

pares = {x: x**2 for x in range(10) if x % 2 == 0}
print(pares)


# A partir de listas
nomes = ["Ana", "Bruno", "Carlos"]
idades = ["20", "25", "30"]

dicionario = {nome : idade for nome, idade in zip(nomes, idades)}
print(dicionario)


# Modificando valores de um dicionário existente
precos = {"banana": 3, "maçã": 7, "laranja": 6}
print(precos)

novos_precos = {k : n*1.4 for k, n in precos.items()}
print(novos_precos)
