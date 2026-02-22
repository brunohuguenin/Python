cores = ("vermelho", "azul", "verde")
print(cores[2])

# método count() - pecorre a tupla e retorna a quantidade
# de vezes que o elemento aparece

# método index() - retorna o índice (posição) do eloemento

frutas = ("uva", "melância", "goiaba", "uva", "maçã", "abacate", "uva", "melância", "pêra")

print(frutas.count("uva"))
print(frutas.count("melância"))
print(frutas.count("goiaba"))

print(f"índice de abacate: {frutas.index("abacate")}")