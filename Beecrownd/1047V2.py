n = input().split()
a, c, b, d = map(int, n)

hour_initial = a * 60 + c
hour_end = b * 60 + d
hours = 0
if hour_initial > hour_end or hour_initial == hour_end:
    hours =  (24 * 60) - (hour_initial - hour_end)
else: 
    hours = hour_end - hour_initial
print(f"O JOGO DUROU {hours // 60} HORA(S) E {hours % 60} MINUTO(S)")
