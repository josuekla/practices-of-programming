n = input().split()
a, c, b, d = map(int, n)

hours = 0
minutes = 0

if a == b:
    if c == d:
        hours = 0
        minutes = 0
    if c > d:
        hours = 24
        minutes = 60 - (c - d)
    else:
        hours = 24
        minutes = d - c
elif a < b:
    if c == d:
        hours = b - a
    elif c > d:
        hours = b - a - 1
        minutes = 60 - (c - d)
    elif c < d:
        hours = b - a
        minutes = d - c
else:
    if c > d:
        minutes = (60 - c) + d
        hours = 24 - a - b + 1
    elif c < d:
        hours = 24 - (a - b)
        minutes = c + d

print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")