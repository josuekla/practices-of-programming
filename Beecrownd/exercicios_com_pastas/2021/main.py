valor = float(input())
total_em_centavos = int(valor * 100)

nota100 = total_em_centavos // 10000
total_em_centavos %= 10000

nota50 = total_em_centavos // 5000
total_em_centavos %= 5000

nota20= total_em_centavos // 2000
total_em_centavos %= 2000

nota10 = total_em_centavos // 1000
total_em_centavos %= 1000

nota5 = total_em_centavos // 500
total_em_centavos %= 500

nota2 = total_em_centavos // 200
total_em_centavos %= 200




nota1 = total_em_centavos // 100
total_em_centavos %= 100


coin_50 = total_em_centavos // 50
total_em_centavos %= 50

coin_25 = total_em_centavos // 25
total_em_centavos %= 25

coin_10 = total_em_centavos // 10
total_em_centavos %= 10

coin_5 = total_em_centavos // 5
total_em_centavos %= 5

coin_1 = total_em_centavos // 1
print("NOTAS:")
print(f"{nota100:.0f} nota(s) de R$ 100.00")
print(f"{nota50:.0f} nota(s) de R$ 50.00")
print(f"{nota20:.0f} nota(s) de R$ 20.00")
print(f"{nota10:.0f} nota(s) de R$ 10.00")
print(f"{nota5:.0f} nota(s) de R$ 5.00")
print(f"{nota2:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{nota1:.0f} moeda(s) de R$ 1.00")
print(f"{coin_50:.0f} moeda(s) de R$ 0.50")
print(f"{coin_25:.0f} moeda(s) de R$ 0.25")
print(f"{coin_10:.0f} moeda(s) de R$ 0.10")
print(f"{coin_5:.0f} moeda(s) de R$ 0.05")
print(f"{coin_1:.0f} moeda(s) de R$ 0.01")