# Dada uma lista de nomes, imprima cada nome em uma linha.

listaNomes = []

print("Digite os nomes (ou digite 'sair' para encerrar): ")

while True:
  entrada = input("Nome: ")

  if entrada. lower() == "sair":
    break

  listaNomes.append(entrada)

print("\n=== LISTA FINAL DE NOMES ===")
for nome in listaNomes:
  print(nome)