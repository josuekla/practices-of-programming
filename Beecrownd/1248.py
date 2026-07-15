import re


test_case = int(input())

for _ in range(test_case):
    diet_aplha = input()
    moment_1 = input()
    moment_2 = input()

    final_diet = (diet_aplha).replace((moment_1+moment_2))
    # print(re.sub(moment_1+moment_2), diet_aplha)
    print(final_diet)

    # miss_aliment = []
    # for letter in diet_aplha:
    #     for letter_m1 in moment_1:
    #         if letter_m1 != letter:
    #             miss_aliment.append(letter_m1)

    #     for letter_m2 in moment_1:
    #         if letter_m2 != letter:
    #             miss_aliment.append(letter_m2)
    # print(miss_aliment)