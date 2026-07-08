test_case = int(input())
total_sequence = 0
current_number = 0
# numbers_sequence  = []
numbers_sequence  = []

for i in range(test_case):
    numbers_sequence.append(int(input()))

for idx in range(0, len(numbers_sequence)):
    if idx == 0 and numbers_sequence[idx] == 1:
        total_sequence += 1
        print("Primeiro Número sendo 1")

    if idx + 1 < len(numbers_sequence):
        # print(numbers_sequence[idx])
        print("\n\nCurrent Number:", numbers_sequence[idx])
        print("Next Number:", numbers_sequence[idx + 1])
        if numbers_sequence[idx] != numbers_sequence[idx + 1]:
            total_sequence += 1
    else:
        print('Ultimo numero é o ', numbers_sequence[idx])



    print("TOTAL SEQUENCE:", total_sequence)
    print("INDEX:", idx)

print(total_sequence)