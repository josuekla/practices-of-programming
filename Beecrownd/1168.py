test_case = int(input())

total_leds = []

while test_case > 0:
    
    mappers_numbers = {
        "1" : 2,
        "2" : 5,
        "3" : 5,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 3,
        "8" : 7,
        "9" : 6,
        "0" : 6
    }
    number_leds_input = input()
    
    total_leds_individual = 0
    for number in number_leds_input:
        if number in mappers_numbers.keys():
            total_leds_individual += mappers_numbers.get(number)
            
    
    total_leds.append(total_leds_individual)
    
    
    test_case -= 1
    
    
for numbers_leds in total_leds:
    print(numbers_leds, "leds") 