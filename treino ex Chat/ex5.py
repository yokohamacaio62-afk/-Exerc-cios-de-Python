lista = "computador"

vogais = []
consoantes = []

for letras in (lista):
    if letras in "aeiou":
        vogais.append(letras)
    else:
        consoantes.append(letras)

print ("vogais:, ", vogais)
print("consoantes:, ", consoantes)