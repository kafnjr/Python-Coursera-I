num = int(input("Digite o valor de n: "))

def fatorial(n):
    fatorial = n
    if n == 0:
        fatorial = 1
        print(fatorial)
    else:
        while (n > 1):
            fatorial = fatorial * (n-1)
            n -= 1
        print(fatorial)

fatorial(num)
