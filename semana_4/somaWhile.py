num = int(input("digite o número: "))
soma, total = 0,0


while (num > 0):
    soma = num%10
    num = num//10
    total += soma
print('total', total)
