n = input().split()
a, b = map(int, n)

if a > b or a == b:
    time =  24 - (a - b)
else: 
    time = b - a

print(f"O JOGO DUROU {time} HORA(S)")