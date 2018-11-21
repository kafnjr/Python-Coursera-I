n = int(input("Digite o valor de n: "))
p = int(input("Digite o número de p: "))

def fatorial(n):
    fatorial = n
    if n == 0:
        fatorial = 1
        return fatorial
    else:
        while (n > 1):
            fatorial = fatorial * (n-1)
            n -= 1
        return fatorial

def coef_binomial(n , p):
    num = fatorial(n)
    k = fatorial(p)
    sub = fatorial((n-p))
    calc = num/(k*sub)
    return calc

coeficiente = coef_binomial(n , p)
print(coeficiente)
