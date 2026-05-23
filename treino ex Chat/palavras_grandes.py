frase = "python e muito divertido e legal"
texto = frase.split()

def contar_palavras_grandes():
    contador = 0
    for palavra in texto:
        if len (palavra) > 5:
            contador += 1 
    return contador
print(contar_palavras_grandes())
