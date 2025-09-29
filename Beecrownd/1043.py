n = input().split()
a, b, c = map(float, n)

if a + b > c and a + c > b and b + c > a:
    print("Perimetro =", a + b + c)
else:
    print("Area =", (a + b) * c / 2)
