while  True:
    value = input().split()
    m, n = map(int, value)
    if m <= 0 or n <= 0:
        break
    maior = n
    menor = m
    if m > n:
        maior = m
        menor = n
    soma = 0 
    for i in range(menor, maior + 1):
        soma += i
        print(i, end=' ')
    print(f"Sum={soma}")

