import sys

argc = len(sys.argv)
if argc != 2:
    print("usage: resgister_names.py <FILE>")
    exit(-1)

filename = sys.argv[1]
name_file = open(filename, "wt")

while True:
    name = input()
    if name == '':
        break
    name_file.write(f"{name}\n")

name_file.close()

row = 0

names_files = open(filename, 'rt')
for line in names_files.readlines():
    row += 1
    print(f'{row}: {line}', end="")
names_files.close()