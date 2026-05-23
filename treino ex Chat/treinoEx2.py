lista = [-5, 8, -2, 10, 0, -7]

negativos = []
positivos = []

def lista_postivos_e_negativos():
    for numero in (lista): 
        if numero >= 0:
            positivos.append(numero)
        elif numero <= 0:
            negativos.append(numero)
        else:
            print("invalido")

print("positivos: , ", positivos)
print("negativos: , ", negativos )