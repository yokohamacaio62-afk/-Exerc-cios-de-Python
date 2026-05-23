lista = [5, 8, 2, 10, 3]

def maior_numero (lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior