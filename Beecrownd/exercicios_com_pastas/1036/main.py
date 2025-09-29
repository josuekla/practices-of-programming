import math
n = input().split()
a, b, c = map(float, n)

delta = b ** 2 - (4 * a * c)


if a > 0 and delta > 0:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
else:
    print("Impossivel calcular")