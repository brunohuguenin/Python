# Verifique se um determinado valor existe dentro de uma tupla usando loop.

val = (3, 13, 27, 33, 47, 53, 67)

valor_na_tupla = int(input("Qual o valor você quer saber se há na tupla?: "))

for i in val:
  if valor_na_tupla == i:
    print(f"O valor {valor_na_tupla} se encontra na tupla na posição: {val.index(i)}")
    break
  else:
    print(f"O valor {valor_na_tupla} não se encontra na tupla")
