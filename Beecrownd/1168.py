LEDS = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6
}

test_case = int(input())

for _ in range(test_case):
    number = input()
    total = sum(LEDS[digit] for digit in number)
    print(total, "leds")