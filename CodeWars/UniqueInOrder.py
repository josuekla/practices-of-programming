def unique_in_order(sequence):
    list_chars = []
    if len(sequence) == 0:
        return list(sequence)
    if isinstance(sequence[0], str) or isinstance(sequence[0], int):
        for index, chars in enumerate(sequence):
            if index == 0 or chars != list_chars[len(list_chars) - 1]:
                list_chars.append(chars)
        return list_chars
    else:
        return list_chars


# unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
print(unique_in_order("AABBCCDDEEaaaGGGHHH"))

# print("A empty list: ()", unique_in_order(()))
# print("A empty list: []", unique_in_order([]))
# print("A empty list: '' ", unique_in_order(""))
# print("A just a char : ", unique_in_order("A"))
# print("A just a char with tuble: ", unique_in_order(("A",)))
# print("A just a char with list: ", unique_in_order(["A"]))

# print("A string with the same doubles chars [AA]: ", unique_in_order("AA"))
# print("A string with the same doubles chars with differents chars [AAAABBBCCDAABBB]: ", unique_in_order("AAAABBBCCDAABBB"))
# print("A string with the same doubles chars with differents chars in case sensitives [ABBCcA]: ", unique_in_order("ABBCcA"))
# print("Sequence of numbers [1, 2, 3, 3, -1]: ", unique_in_order([1,2,2,1]))
# print("Sequence of chars ['a', 'b', 'b', 'a']: ", unique_in_order(["a", "b", "b", "a"]))