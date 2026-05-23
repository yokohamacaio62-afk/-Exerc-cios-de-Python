lista = [1, 2, 3, 4]
soma = 0 

def somar_lista (lista):
    soma = 0 
    for numero in lista:
        soma += numero
    return(soma)

print(somar_lista(lista))