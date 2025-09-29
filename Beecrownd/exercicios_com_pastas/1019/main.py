days = int(input())
year = days // 365
month = (days % 365) // 30
day = (days % 365) % 30   

print(f"{year} anos(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")
