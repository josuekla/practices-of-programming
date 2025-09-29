num = int(input())
ddd = (61, 'Brasilia'), (71, 'Salvador'), (11, 'Sao Paulo'), (21, 'Rio de Janeiro'), (32, 'Juiz de Fora'), (19, "Campinas"), (27, 'Vitoria'), (31, "Belo Horizonte")
result = 'DDD nao cadastrado'

for i in ddd:
    if num == i[0]:
        result = i[1]
print(result)