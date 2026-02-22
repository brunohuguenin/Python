# Para transformar uma estrutura na outra, usamos as funções integradas list() e tuple().

numeros_primos = (2,3,5,7,11,13,17,19,23,29)
print("Tupla:")
print(numeros_primos)

# Convertendo para lista para poder alterar os dados

n_primos_list = list(numeros_primos)
print("Lista:")
print(n_primos_list)

n_primos_list.append(31)
n_primos_list.append(37)
n_primos_list.insert(0, "Números Primos")
print(n_primos_list)
n_primos_list.remove("Números Primos")
print(f"Lista com a String Removida:\n{n_primos_list}")

# Convertendo de volta a lista em tupla
n_primos_tuple = tuple(n_primos_list)
print(f"Lista convertida em tupla:\n{n_primos_tuple}")

print("-------------------------------------------------")
# Registro de uma funcionária
funcionario = ("Alice", 30, "Desenvolvedora Jr")
print(funcionario)

# ela foi promovida!
temp_list = list(funcionario)
temp_list[2] = "Desenvolvedora Senior"
funcionario = tuple(temp_list)
print(funcionario)