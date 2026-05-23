frase = "python e muito divertido"
palavras = frase.split()

def menor_palavra ():
    menor = palavras[0]

    for palavra in palavras:
        if len (palavra) < len (menor):
            menor = palavra

    return menor
print("A menor palavra é:, ", menor_palavra())
