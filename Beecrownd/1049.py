question1 = input()
question2 = input()
question3 = input()


if question1 == "vertebrado":
    if question2 == "ave":
        if question3 == "onivoro":
            result = 'pomba'
        else:
            result = 'aguia'
    else:
        if question3 == "onivoro":
            result = 'homem'
        else:
            result = 'vaca'
else:
    if question2 == "inseto":
        if question3 == 'herbivoro':
            result = 'lagarta'
        else:
            result = "pulga"
    else:
        if question3 == "onivoro":
            result = 'minhoca'
        else:
            result = 'sanguessuga'

print(result)