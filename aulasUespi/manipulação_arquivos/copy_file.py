import sys

argc = len(sys.argv)
if argc != 3:
    print(f'usage: {sys.argv[0]} <source file> <copy text>')
    exit(-1)

with open(sys.argv[1], 'rb') as file_input, open(sys.argv[2], 'wb') as file_output:
    block_bytes_readed = 1024
    while text_readed := file_input.read(block_bytes_readed): #while the text_readed return TRUE and text_readed receveive the value
        file_output.write(text_readed)
        if len(text_readed) < block_bytes_readed: break
    
print("\nARQUIVOS COPIADOS COM SUCESSO!")

