# encoding: utf-8
#n -> peças na mesa do jogo
#m -> peças a serem retiradas
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
    if camp == 1:
        partida()
    else:
        campeonato()

def computador_escolhe_jogada(n, m):
    '''Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador de acordo com a estratégia vencedora.'''
    if n >= m and (n%(m+1)) == 0:
        return m
    elif (n%(m+1)) != 0:
        return (n%(m+1))
    elif n == m:
        return m
    elif n < m:
        return n


    #tem que devolver o número de peças removidas pela jogada


def usuario_escolhe_jogada(n, m):
    '''Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.'''
    jog = int(input("Quantas peças você vai tirar? "))
    while (jog <= 0 or jog > m) or jog > n:
        print("\nOops! Jogada inválida! Tente de novo.\n\n")
        jog = int(input("Quantas peças você vai tirar?"))
    return jog #tem que devolver o número de peças removidas pela jogada

def partida():
    '''Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.'''
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogadas? "))
    cont = 0
    player = 1
    pecas_ret = 0
    pecas_restantes = 0
    placar_comp = 0
    placar_jogador = 0

    while True:
        while (n%(m+1)) == 0 and cont < 1:
            print("Você começa!")
            cont += 1
            pecas_ret = usuario_escolhe_jogada(n, m)
            pecas_restantes = n - pecas_ret
            n = pecas_restantes
            print("Você tirou",pecas_ret,"peça(s).\nAgora resta apenas",pecas_restantes,"peças no tabuleiro\n\n\n")
        if player == 1:
            cont += 1
            pecas_ret = computador_escolhe_jogada(n, m)
            pecas_restantes = n - pecas_ret
            n = pecas_restantes
            player = 2
            print("O computador retirou",pecas_ret,"peça(s).\nAgora resta apenas",pecas_restantes,"peças no tabuleiro\n\n\n")
            if n == 0:
                print("O computador ganhou!\n\n")
                placar_comp += 1
                break
        else:
            pecas_ret = usuario_escolhe_jogada(n, m)
            pecas_restantes = n - pecas_ret
            n = pecas_restantes
            player = 1
            print("Você tirou",pecas_ret,"peça(s).\nAgora resta apenas",pecas_restantes,"peças no tabuleiro\n\n\n")
            if n == 0:
                print("Você ganhou!\n\n")
                placar_jogador += 1
                break
        if n == 0:
            break
    print("Placar: Você:",placar_jogador,"X",placar_comp,":Computador")



def campeonato():

    '''Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma: Placar: Você ??? X ??? Computador'''
    rodada = 0
    while rodada < 3:
        print("**** Rodada",rodada+1," ****")
        rodada += 1
        partida()


main()
