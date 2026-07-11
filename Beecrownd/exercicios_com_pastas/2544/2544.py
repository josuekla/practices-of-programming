try:
    while True:
        count = 0
        a = int(input())
        while a != 1:
            a = a // 2
            count += 1
        # print(0) if a == 1 else print(round(a // 2))
        print(count)
except EOFError:
    pass