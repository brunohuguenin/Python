# Dicionários aninhados

usuarios= {
  "user1": {
    "nome":"Bruno",
    "idade":25,
    "cidade":"Rio"
  },
  "user2": {
    "nome":"Ana",
    "idade":30,
    "cidade":"São Paulo"
  }
}
'''
print(usuarios["user1"]["nome"])

# Iterando sobre dicionários aninhados
for user, info in usuarios.items():
  print(user)

for chave, valor in usuarios.items():
  print(f"{chave}: {valor}")


# Modificando valores
usuarios["user1"]["idade"] = 26
print(usuarios["user1"])


# Adicionando novos valores
usuarios["user1"]["email"] = "bruno@gmail.com"
print(usuarios["user1"])


# Adicionando novos itens completos

usuarios["user3"] = {
  "nome": "Carlos",
  "idade": 30,
  "cidade": "Curitiba"
}
print(usuarios["user3"])
'''

# Padrão tipo JSON
pedido= {
    "id":1,
    "cliente": {
    "nome":"Bruno",
    "email":"bruno@email.com"
    },
  "itens": [
          {"produto":"Notebook","preco":3000},
          {"produto":"Mouse","preco":100}
      ]
}

print(pedido)