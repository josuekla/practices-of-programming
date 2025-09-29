test_case = int(input())
for _ in range(test_case):
    anos = 0
    values = input().split()
    population_a, population_b = map(int, values[:2])
    grow_a, grow_b = map(float, values[2:])
    

    while population_a <= population_b:
        population_a += int(population_a * (round(grow_a, 5) / 100))
        population_b += int(population_b * (round(grow_b, 5) / 100))
        anos += 1
        

if anos <= 100:
    print(f"{anos} anos.")
else:
    print(f"Mais de 1 seculo.")

