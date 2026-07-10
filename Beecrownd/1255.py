test_case = int(input())

for _ in range(test_case):
    dict_qtn = {}
    word = input().lower()
    for l in word:
        if l.isalpha():
            if l in dict_qtn.keys():
                dict_qtn[l] += 1
            else:
                dict_qtn[l] = 1
            
    maior_valor = max(dict_qtn.values())
    todos_maiores = [key for key, value in dict_qtn.items() if value == maior_valor]
    letras_maiores = "".join(sorted(todos_maiores))
    print(letras_maiores)

            
            
            
