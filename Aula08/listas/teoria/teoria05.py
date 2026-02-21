# List Comprehensions

# Transformação direta
'''
numeros = [1, 2, 3, 5, 7, 11, 13]
quadrados = [n**2 for n in numeros]

print(quadrados)

frutas = ["maÇÃ", "banana", "CEREJA", "Uva", "aBACAXI"]
formatar_frutas = [f.lower() for f in frutas]

print(formatar_frutas)
'''

# ---------------------------------------
# Decidindo o que irá entrar na nova lista
'''
numeros = range(20)
pares = [x for x in numeros if x % 2 == 0]

print(pares)

palavras = ["Python", "oi", "IA", "desenvolvimento"]
longas = [p for p in palavras if len(p) > 5]

print(longas)
'''

# ---------------------------------------
# Condições complexas
notas = [4, 7, 5, 8.3, 9, 6.8]
status = ["Aprovado" if n >= 7 else "Reprovado" for n in notas]

print(status)