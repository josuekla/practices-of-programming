def soma(x_value, array):
    return x_value + array

def sub(x_value, array):
    return x_value - array

def mul(x_value, array):
    return x_value * array

def div(x_value, array):
    return x_value // array

def make_operation() -> None:
    possibles_numbers.clear()
    min_diff.clear()
    for i in range(N):
        possibles_numbers.append(soma(X, A[i]))
        possibles_numbers.append(sub(X, A[i]))
        possibles_numbers.append(mul(X, A[i]))
        possibles_numbers.append(div(X, A[i]))
        
    for number in possibles_numbers:
        min_diff.append(abs(number - Y))
    
def result_X() -> int:
    return possibles_numbers[min_diff.index(min(min_diff))]
    

X, Y, N = map(int, input().split())

A = list(map(int, input().split()))

print(f"X {X}")
print(f"Y {Y}")
print("A: ", A)

possibles_numbers = []
min_diff = []
min_attemps = 0
attemps = 0

while X != Y:
    make_operation()
    X = result_X()
    min_attemps += 1
    if min_attemps == 15:
        min_attemps = -1
        break
    
print(min_attemps)

# make_operation()
# X = result_X()
# print(possibles_numbers)
# print(f"X {X}")
# print("MINDIFF", min_diff)

# make_operation()
# print(possibles_numbers)
# print(result_X())
# print("MINDIFF",min_diff)

# X = result_X()
# print(f"X {X}")




    # X = result_X

# for number in possibles_numbers:
#     min_diff.append(abs(number - Y))
    
    # print(f"operation: {number} - {Y}",)
    # print("DIFF:", min_diff)
    # print(f"NUMBER CHOICE:", number_choice)
    

# print(min_diff)
# print(possibles_numbers)

# print(min(min_diff))
# print(min_diff.index(min(min_diff)))
# print(possibles_numbers[min_diff.index(min(min_diff))])


# print("X:",X)
# print("Y:",Y)
# print("N:",N)
