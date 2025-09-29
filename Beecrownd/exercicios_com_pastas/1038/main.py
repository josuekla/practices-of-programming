code_list = (4.00, 4.50, 5.00, 2.00, 1.50)
n = input().split()
product_code, qtd = map(int, n)

print(f"Total: R$ {code_list[product_code - 1] * qtd:.2f}")
