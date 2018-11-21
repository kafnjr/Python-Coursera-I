num = int(input("Digite um número: "))
lista = []
list = []

def listaZero(num):
    if (num % 10) == 0:
        list.append(num)
    return list

while num != 0:
    lista = listaZero(num)
    num = int(input("Digite um número: "))
lista.reverse()
print(lista)
