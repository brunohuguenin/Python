# Criando um dicionário

carro = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}

print(carro["marca"])
print(carro.get("ano"))

# Para acessar uma informação que você não tem certeza que existe
# no dicionário, o mais apropriado é usar o .get(), pois caso não exista reamente
# retorna uma mensagem ao invés de travar o programa

print(carro.get("cor", "Não encontrado"))
print(carro.get("modelo", "Não encontrado"))




# Adicionando e removendo valores
carro["cor"] = "Vermelho"
print(carro)

del carro["ano"]
print(carro)

carro.pop("modelo")
print(carro)
