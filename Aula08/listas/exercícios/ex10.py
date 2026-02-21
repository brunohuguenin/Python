# Verifique se uma lista está em ordem crescente.

def esta_crescente(lista):
  if len(lista) < 2:
    return True
  
  for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
      return False
  return True

numeros = [1,5,10,15,20,35,30]
print(f"Lista: {numeros}")

if esta_crescente(numeros) == True:
  print("A lista está ordenada.")
else:
  print("A lista não está ordenada.")