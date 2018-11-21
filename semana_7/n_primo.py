num = int(input("Digite um número inteiro: "))

def n_primo(n):
        num = n - 1
        i = 2
        cont = 0
        if n == 1 or n == 0:
            return 0
        else:
            while i <= num:
                while num > 1:
                    result = i % num
                    if result == 0:
                        cont += 1
                    else:
                        cont += 0
                    num -= 1
                i += 1
            if cont != 0:
                return cont

imp = n_primo(num)
print(imp)
