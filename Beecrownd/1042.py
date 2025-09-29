n = input().split()
num1, num2, num3 = map(int, n)
lista_num = [num1, num2, num3]
lista_sort = lista_num.copy()
lista_sort.sort()
for i in lista_sort:
    print(i)
print()
for i in lista_num:
    print(i)