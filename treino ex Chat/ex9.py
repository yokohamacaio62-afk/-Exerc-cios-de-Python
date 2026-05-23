lista = "computador"


def contar_vogais (lista):
    contador = 0
    for letra in (lista):
        if letra in "aeiou":
            contador += 1
    return contador
print(contar_vogais(lista))

