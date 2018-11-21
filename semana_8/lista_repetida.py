lista = [1, 1, 3, 4, 5, 6, 6, 7, 8, 9]

def remove_repetidos(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista


lista_ord = remove_repetidos(lista)

print(sorted(lista_ord))
