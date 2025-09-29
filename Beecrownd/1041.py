n = input().split()
x, y = map(float, n)


if x == 0 or y == 0:
    if y != 0:
        print("Eixo Y")
    elif x != 0:
        print("Eixo X")
    else:
        print("Origem")
        
    
else:
    if x > 0 :
        if y > 0:
            print("Q1")
        elif y < 0:
            print("Q4")
        
    else:
        if y > 0:
            print("Q2")
        elif y < 0:
            print("Q3")
        

