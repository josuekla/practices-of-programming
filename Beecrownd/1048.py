salary = float(input())

if salary <= 400:
    percentual = 15
    new_salary = (15 / 100) * salary 
elif salary <= 800:
    percentual = 12
    new_salary = (12 / 100) * salary 
elif salary <= 1200:
    percentual = 10
    new_salary = (10 / 100) * salary 
elif salary <= 2000:
    percentual = 7
    new_salary = (7 / 100) * salary 
else:
    percentual = 4
    new_salary = (4 / 100) * salary 


print(f"Novo salario: {new_salary + salary:.2f}")	
print(f"Reajuste ganho: {new_salary:.2f}")	
print(f"Em percentual: {percentual:.0f} %")	

