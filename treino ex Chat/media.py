notas = (7,8,10)

def calcular_media (notas):
    soma = 0

    for nota in notas:
        soma += nota

    media = soma/len(notas)

    return(media)
print ("a media deu:", calcular_media(notas))

