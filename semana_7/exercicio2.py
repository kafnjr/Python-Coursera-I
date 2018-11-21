largura = int(input("digite  a largura: "))
altura = int(input("digite a altura: "))

linha = 1
coluna = 1

while linha <= altura:
    while coluna <= largura:
        if ((linha > 1) and (coluna > 1)) and ((linha < altura) and (coluna < largura)):
            print(" ", end="")
        else:
            print("#", end="")
        coluna += 1
    linha += 1
    print("")
    coluna = 1

