import re

pattens = [r'\.']

test_case = int(input())

for _ in range(test_case):
    s1, s2 = input().split()
    # print(s1, s2)
    letter_formatter = []
    # print("LISTA INICIAL:", letter_formatter)
    for index in range(max(len(s1) , len(s2))):
        if index < len(s1):
            letter_formatter.append(s1[index])
        if index < len(s2):
            letter_formatter.append(s2[index])
        # print(f"{index} LISTA em indice: ", letter_formatter)

    # print("LISTA FINAL:", letter_formatter)
    # print("LISTA formatada:", "".join([*letter_formatter]))
    print("".join([*letter_formatter]))
    