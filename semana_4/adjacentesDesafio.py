num = int(input('Digite o número inteiro: '))
verificador = 0
primeiro, segundo= 0,0
cont = 0
while (num > 0):
    segundo = num%10
    num = num//10
    primeiro = segundo
    segundo = num%10
    if (primeiro == segundo):
        verificador += 1
    cont += 1
    print('primeiro(',cont,')',primeiro)
    print('segundo(',cont,')',segundo)
if verificador >= 1:
    print('sim')
else:
    print('não')
