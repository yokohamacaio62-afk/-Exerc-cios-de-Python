lista = [8, 3, 15, 1, 9]

def menor_numero (lista):
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor