# Principais métodos

nomes = ["Bruno", "Ana", "Carlos", "Francisco", "Chiquinha"]
print(f"Lista Original:\n{nomes}\n")

nomes.append("Robervaldo")
print(f"Adicionando valor:\n{nomes}\n")

nomes.remove("Carlos")
print(f"Removendo valor específico:\n{nomes}\n")

nomes.pop()
print(f"Removendo o último valor:\n{nomes}\n")

nomes.insert(3, "Samara")
print(f"Adicionando valor em uma posição específica:\n{nomes}\n")

nomes.sort()
print(f"Ordenando os valores:\n{nomes}\n")

nomes.reverse()
print(f"Colocando os valores na ordem inversa:\n{nomes}\n")