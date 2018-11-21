def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato\n")
    camp = int(input(" "))
    while camp != 1 and camp != 2:
        print("\n\nBem-vindo ao jogo do NIM! Escolha:\n\n")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato\n")
        camp = int(input(" "))

def computador_escolhe_jogada(n, m):
    ret = n - (m - (m+1))
def partida():
    #rodad = campeonato()
    print("**** Rodada",rodad,"****")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogadas? "))
main()
