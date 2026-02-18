# Dada uma tupla, conte quantas vezes um valor específico aparece (sem usar count()).

val = (1, 5, 10, 5, 20, 15, 25, 20, 5, 30, 35, 5, 40, 45, 50, 55, 60, 5, 70, 5)

contador = 0

for i in val:
  if i == 5:
    contador += 1

print(f"Tulpa completa {val}")
print(f"Quantidade de elementos 5 na tupla: {contador}")