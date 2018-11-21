lista = [1, 2, 3, 4, 5, 6, 7]

def soma_elementos(lista):
    x = 0
    for i in lista:
        x += i
    return x

soma = soma_elementos(lista)

print(soma)
