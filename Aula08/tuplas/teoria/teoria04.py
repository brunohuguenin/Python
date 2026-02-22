# Tupla mutável - tupla com elemento mutável dentro dela

pessoa = ("Nome", "Carlos", "Notas", [8.5, 9.0])
print(pessoa)

# Mudar um valor da tupla. (ERRO)
# pessoa[0] = "João"  -> ERRO

# Mudar um valor dentro da lista
pessoa[3].remove(8.5)
pessoa[3].insert(0, 10.0)
print(pessoa)

