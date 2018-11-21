while True:
    num = int(input("Digite um número: "))
    fatorial = num
    if num == 0:
        fatorial = 1
        break
    while num > 1:
        fatorial = fatorial * (num - 1)
        num -= 1

    print(fatorial)
