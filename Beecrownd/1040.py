n = input().split()
n1, n2, n3, n4 = map(float, n)

average = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
situation = ''

if average >= 7:
    print(f"Media: {average:.1f}")
    print("Aluno aprovado.")
elif average >= 5:
    print(f"Media: {average:.1f}")
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam}")
    average = (exam + average) / 2
    if average >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {average:.1f}")
else:
    print(f"Media: {average:.1f}")
    print("Aluno reprovado.")
    