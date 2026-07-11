test_case = int(input())

for _ in range(test_case):
    try:
        input_letter = input()
        left_part = input_letter[len(input_letter) // 2 - 1::-1]
        right_part = input_letter[:len(input_letter) // 2 - 1:-1]
        
        print(left_part + right_part)
            
    except:
        print("Deu erro em", _)
        break
         
    
    
    # print("left_part:", left_part)
    # print("right_part:",right_part)