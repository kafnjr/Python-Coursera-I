def main():
    n = int(input("Digite um número inteiro: "))
    if n >= 0:
        fatorial(n)
    #     i -= 1

def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    #n = int(input("Digite um número inteiro: "))
    main()

main()
