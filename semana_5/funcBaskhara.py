from math import sqrt
a = int(input("Digite o valor de x²: "))
b = int(input("Digite o valor de x: "))
c = int(input("Digite o número natural: "))

def delta(a, b, c):
    valor = (b**2)-(4*a*c)
    return valor

def Funcbaskhara(a, b, c):
    dlta = delta(a, b, c)

    if dlta > 0:
        x1 = (-(b)+sqrt(dlta))/(2*a)
        x2 = (-(b)-sqrt(dlta))/(2*a)
        print("O valor de x¹ é:", x1,"O valor de x² é:", x2)
    elif dlta == 0:
        x = (-(b)+sqrt(dlta))/(2*a)
        print("O valor de x é:", x)
    else:
        print("A raiz não possui valores reais!")

Funcbaskhara(a, b, c)
