# Use um loop para calcular a soma dos elementos de uma tupla (sem usar sum()).

val = (1,5,10,15,20,25)

somaTotal = 0

for i in val:
  somaTotal += i

print(f"Tulpa completa {val}")
print(f"Soma dos elementos da tupla: {somaTotal}")