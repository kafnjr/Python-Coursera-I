import math
num_x1 = int(input("Digite o valor de x1: "))
num_y1 = int(input("Digite o valor de y1: "))
num_x2 = int(input("Digite o valor de x2: "))
num_y2 = int(input("Digite o valor de y2: "))
d = math.sqrt(((num_x2-num_x1)**2)+((num_y2-num_y1)**2))
if d >= 10:
    print("longe")
else:
    print("perto")
