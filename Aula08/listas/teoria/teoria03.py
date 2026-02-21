# Imprimindo lista dentro de lista
'''
dados = [
  ["Ana", "Bruno", "Carlos"],
  ["Maria", "João"],
  ["Marcos", "Henrique"],
  ["Wesley"]
]

for sublista in dados:
  for valor in sublista:
    print(valor)
'''

# ----------------------------------------------------
# Imprimir com índice da lista externa e interna

'''
dados = [
  ["Ana", "Bruno", "Carlos"],
  ["Maria", "João"],
  ["Marcos", "Henrique"],
  ["Wesley"]
]


for i, sublista in enumerate(dados):
  for j, valor in enumerate(sublista):
    print(f"[{i}][{j}] = {valor}")
'''

# ----------------------------------------------------
# List com tipos mistos
'''dados = ["Ana", ["Bruno", "Carlos"], "Maria", ]

# Forma errada de imprir String, já que é iterável, irá quebrar letra por letra
# Observação: int e boolean não são iteráveis!
for item in dados:
    for x in item:
        print(x)

# Forma correta de imprimir uma lista mista
for item in dados:
  if isinstance(item, list):
     for x in item:
        print(x)
  else:
    print(item)
'''

# ----------------------------------------------------
# Listas aninhadas em vários níveis (recursão)
# se a profundidade não é previsível

dados = [1, [2, [3, 4], 5], 6]

def imprimir_lista(lista):
  for item in lista:
    if isinstance(item, list):
      imprimir_lista(item)
    else:
      print(item)

imprimir_lista(dados)