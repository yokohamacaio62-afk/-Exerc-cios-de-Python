frase = "python e muito divertido"
palavras = frase.split()

def encontrar_maior_palavra():
    maior = palavras[0]

    for palavra in palavras:
        if len (palavra) > len (maior):
            maior = palavra

    return maior

print(encontrar_maior_palavra())