import re

pattern = re.compile(r'^[A-Za-z]+\.?$')

def is_word(simbolo:str):
    if simbolo.endswith('.'):
        simbolo = simbolo[:-1]
        
    return simbolo.isalpha()


while True:
    try:
        words = input().split()

        valid = [w for w in words if pattern.fullmatch(w)]

        total_sum = sum(
            len(w.rstrip('.')) for w in valid
        )

        avg = total_sum // len(valid) if valid else 0
        
        if len(words) == 0:
            print(0)
            continue

        if avg <= 3:
            print(250)
        if 4 <= avg <= 5:
            print(500)
        if avg >= 6:
            print(1000)

    except EOFError:
        break
        
        # words_formatters = [word for word in words if not bool(re.search(r'\d', word) or word.count('.') > 2) ]
        # words_formatters_n = [word for word in words if bool(re.search(r'\d', word) or not word.count('.') > 2) ]
        # print("LISTA ORIGINAL: ", words)
        
        # words = words_formatters
        
        # print("DEPOIS DE FORMATAR: ", words)
        
        # print("SImbolos que tem apenas letras:", words_formatters)
        # print("SImbolos que tem apenas letras + Numeros + > 2 '.':", words_formatters_n)         
    
        # sum_len_words = sum(len(word) for word in words)
        
        # number_of_words = len(words)
        
        # if len(words) == 0:
        #     average_len = 0
        # else:
        #     average_len = sum_len_words // number_of_words

        # if average_len <= 3:
        #     print("250")
        # if 4 <= average_len <= 5:
        #     print("500")
        # if average_len >= 6:
        #     print("1000")
        
        # print("Soma do tamanho das letras:",sum_len_words)
        # print("Tamanho das letras total", len(words))
        # print(average_len)
    # except EOFError:
    #     break