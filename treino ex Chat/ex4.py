lista = [3, 5, 9, 10, 12, 14, 15]

divisiveis_por_3 = []

nao_divisiveis = []

for numero in (lista):
    if numero % 3 == 0:
        divisiveis_por_3.append(numero)
    elif numero % 3 >= 1:
        nao_divisiveis.append(numero)
    else:
        print("invalido")

print("Divisíveis por 3: , ", divisiveis_por_3)
print("Nao_divisiveis: ," , nao_divisiveis)