def primo(n):
        div = 0
        for i in range(2, n+2):
            fator = (n+2) % i
            if fator == 0:
                div += 1
        if div == 0:
             return True
        else:
            return False

def maior_primo(num):
    Mnum = 0
    if num != 1 and num != 0 and num != 2:
        for i in range(0, num+2):
            verif = primo(i)
            if verif:
                Mnum = i
        return Mnum
    elif num == 2:
        return 2
    else:
        return "Favor digitar valor maior ou igual a 2!"

print(maior_primo(7))
