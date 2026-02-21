# Verifique se um determinado valor existe em um conjunto.

num = {10,15,20,25,30,35,40,45,50}

valor_na_set = int(input("Qual o valor você quer saber se há no conjunto?: "))

if valor_na_set in num:
    print(f"O valor {valor_na_set} se encontra no conjunto")
else:
    print(f"O valor {valor_na_set} não se encontra no conjunto")