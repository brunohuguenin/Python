# Conte quantas vezes um determinado valor aparece em uma lista.

frutas = ["uva", "melância", "goiaba", "uva", "maçã", "abacate", "uva", "melância", "pêra"]
contador = 0
for i in frutas:
  if i == "uva":
    contador += 1

print(f"Lista original: {frutas}")
print(f"A quantidade de vezes que a fruta 'uva' aparece é: {contador}")