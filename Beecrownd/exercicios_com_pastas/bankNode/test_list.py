values = [0] * 7
n = int(input())
while n > 0:
    if n >= 100:
        values[0] += 1
        n -= 100
    elif n >= 50:
        values[1] += 1
        n -= 50
    elif n >= 20:
        values[2] += 1
        n -= 20
    elif n >= 10:
        values[3] += 1
        n -= 10
    elif n >= 5:
        values [4] += 1
        n -= 5
    elif n >= 2:
        values [5] += 1
        n -= 2
    else:
        values [6] += 1
        n -= 1


print(f"{values[0]} nota(s) de R$ 100,00")
print(f"{values[1]} nota(s) de R$ 50,00")
print(f"{values[2]} nota(s) de R$ 20,00")
print(f"{values[3]} nota(s) de R$ 10,00")
print(f"{values[4]} nota(s) de R$ 5,00")
print(f"{values[5]} nota(s) de R$ 2,00")
print(f"{values[6]} nota(s) de R$ 1,00")
