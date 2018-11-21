num = int(input("Digite um número inteiro: "))
result, verif = 0,0
primo = num
if num != 0:
    while num > 0:
        result = primo % num
        if result == 0:
            verif +=1
        num -= 1
    if verif > 2:
        print("não primo")
    else:
        print("primo")
else:
    print("não primo")
