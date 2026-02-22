grade = (1, [2, 3])
try:
    grade[1] += [4]
except TypeError:
    print("Erro disparado!")

print(grade) # Resultado: (1, [2, 3, 4]) -> A lista mudou apesar do erro!