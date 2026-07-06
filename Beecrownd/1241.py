test_case = int(input())

for _ in range(test_case):
    numbers = input()
    number_seq_n1, number_seq_n2 = numbers.split()
    small_sequence  = len(number_seq_n2) if  len(number_seq_n1) > len(number_seq_n2) else len(number_seq_n1)
    
    if len(number_seq_n2) > len(number_seq_n1):
        msg = "nao encaixa"
    else: 
        if number_seq_n1[-small_sequence:] == number_seq_n2[-small_sequence:]:
            msg = "encaixa"
        else:
            msg = "nao encaixa"
            
    print(msg)
        
    
    # msg = "encaixa" if number_seq_n1.endswith(number_seq_n2) else "nao encaixa"
    # print(msg)
    
    # small_sequence  = len(number_seq_n2) if  len(number_seq_n1) > len(number_seq_n2) else len(number_seq_n1)
    # print(small_sequence)
        
    # senquence_1 = -len(number_seq_n2)
    # senquence_2 = -len(number_seq_n2)
    
    # print("Sequence 01:", number_seq_n1[-small_sequence:])
    # print("Sequence 02:", number_seq_n2[-small_sequence:])
    
    # msg = "encaixa" if number_seq_n1[-small_sequence:] == number_seq_n2[-small_sequence:] else "nao encaixa"
    # print(msg)
