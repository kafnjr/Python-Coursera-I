import math
a = float(input("Digite o valor de x²: "));
b = float(input("Digite o valor de x: "));
c = float(input("Digite o valor inteiro da equação: "));

delta = ((b**2)-(4*a*c))

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        x = (-b + math.sqrt(delta))/(2*a)
        print("a raiz desta equação é", x)
    else:
        x_1 = (-b + math.sqrt(delta))/(2*a)
        x_2 = (-b - math.sqrt(delta))/(2*a)
        if x_1 < x_2:
            print("as raízes da equação são", x_1,"e",x_2)
        else:
            print("as raízes da equação são", x_2,"e",x_1)
