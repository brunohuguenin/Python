# Peça um número ao usuário e mostre a tabuada de 1 a 10 desse número.

valor = int(input("Insira um valor para saber sua tabuada de 1 a 10: "))

for i in range(1, 11):
  print(f"{valor} x {i} = {valor * i}")