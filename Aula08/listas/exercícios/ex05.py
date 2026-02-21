# Crie uma nova lista onde cada elemento seja o valor original multiplicado pelo seu índice.

num = [2, -1, 2, 6, 14, -75, -17, 63, 87, 0, 100, 14,-101]
nova_lista = []

for i, valor in enumerate(num):
  resultado = i * valor
  nova_lista.append(resultado)

print(f"A lista original e lista com os valores multiplicados pelo seus índices respectivamente:")
print(f"{num}\n{nova_lista}")