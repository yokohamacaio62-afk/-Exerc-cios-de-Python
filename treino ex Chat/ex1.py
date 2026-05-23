lista = input(["digite uma lista de numeros separados por virgula: "])
lista = lista.split(",")

def somar_lista (lista):
    soma = 0
    for numero in lista:
        soma += (numero)
    return soma 