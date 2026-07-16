stringlaugth = input().lower()
onlyvocals =  [letter for letter in stringlaugth if ord(letter) in [97, 101, 105, 111, 117]]

onlyvocals_reverse = onlyvocals[::-1]
msg = "S" if onlyvocals_reverse == onlyvocals else "N"

print(msg)
# print("LETRAS ORIGINAIS: ", onlyvocals)
# print("LETRAS ORIGINAIS:", onlyvocals_reverse)
# for letter in onlyvocals:
#     print(letter)