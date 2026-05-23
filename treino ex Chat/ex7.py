lista = [4, 15, 8, 22, 10, 3, 18]

maior_que_10 = []
menor_ou_iguais_a_10 = []

for numeros in (lista):
    if numeros > 10: 
        maior_que_10.append(numeros)
    else:
        menor_ou_iguais_a_10.append(numeros)

print("maior_que_10:, ", maior_que_10)
print("menor_ou_iguais_a_10:, ", menor_ou_iguais_a_10)