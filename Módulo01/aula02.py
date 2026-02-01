# TIPOS PRIMITIVOS

# a importancia do tipo primitivo se dá na entrada do usuário,
# pois sem ele, o número que o usuário inserir será convertido 
# em STRING
'''n1 = input("Digite um número: ")

n2 = int(input("Digite um número: "))

print(f"{n1}, {type(n1)}")
print(f"{n2}, {type(n2)}")

print("O primeiro valor inserido foi", n1)'''

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

opcao = int(input("Digite a operacão ue deseja realizar:[1] Adição\n[2] Subtração" \
"\n[3] Multiplicação\n[4] Divisão\n Opção: "))

while opcao < 1 or opcao > 4:
  print("Opção inválida. Tente novamnete!")
  opcao = int(input("Digite a operacão ue deseja realizar:[1] Adição\n[2] Subtração" \
"\n[3] Multiplicação\n[4] Divisão\n Opção: "))
  
match opcao:
  case 1:
    operacao = valor1 + valor2
    print(f"{valor1} + {valor2} = {operacao}")
  case 2:
    operacao = valor1 - valor2
    print(f"{valor1} - {valor2} = {operacao}")
  case 3:
    operacao = valor1 * valor2
    print(f"{valor1} x {valor2} = {operacao}")
  case 4:
    operacao = valor1 / valor2
    print(f"{valor1} / {valor2} = {operacao}")

if valor1 > valor2:
  print(f"O número {valor1} é maior do que {valor2}")
else:
  print(f"O número {valor2} é maior do que {valor1}")


