# encode: UTF-8

def main():

    num = int(input('Digite um número inteiro: '))

    centena = num%1000
    dezena = centena%100
    inteiro = dezena//10
    print('O dígito das dezenas é',inteiro)

main()
