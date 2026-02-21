numeros = [1,2,3,4,5,6]

nomes = ["Ana", "Bruno", "Carlos"]

mista = [1, "Python", "Java", True]

# print(numeros)
# print(nomes)
# print(mista)

for i, valor in enumerate(numeros):
  print(f"{i} - {valor}")

print("--------------------")
for i, valor in enumerate(nomes):
  print(f"{i} - {valor}")

print("--------------------")
for i, valor in enumerate(mista):
  print(f"{i} - {valor}")