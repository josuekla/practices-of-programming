n = input().split()
A, B, C = map(float, n)
list_sort = [A ,B ,C]
list_sort.sort(reverse=True)
A = list_sort[0]
B = list_sort[1]
C = list_sort[2]


if A + B > C and A + C > B and B + C > A:
    if A ** 2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")

    if A ** 2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")

    if A ** 2 < B ** 2 + C ** 2:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")

    if A == B and C != A and C != B or A == C and B != A and B != C or C == B and A != C and A != B: 
        print("TRIANGULO ISOSCELES")

else:
    print("NAO FORMA TRIANGULO")