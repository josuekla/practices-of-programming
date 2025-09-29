# def get_sum(a,b):
#     sum = 0
#     if a > b:
#         for i in range(b, a + 1):
#             sum += i
#     else:
#         for i in range(a, b + 1):
#             sum += i
#     return sum

def get_sum(a,b):
    return sum(range(min(a,b),max(a,b)))

# print(get_sum(3, 3))
# print(get_sum(-1, -1))
print(get_sum(10,110))