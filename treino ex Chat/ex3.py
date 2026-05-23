lista = ["Ana", "Carlos", "João", "Fernanda", "Leo", "Mariana"]

curtos = []
longos = []

for tamanho_de_nome in (lista): 
    if len(tamanho_de_nome) <= 5:
        curtos.append(tamanho_de_nome)
    elif len(tamanho_de_nome) > 5:
        longos.append(tamanho_de_nome)
    else:
        print("invalido")
    
print("Lista de nomes curtos:, " , curtos)
print("lista de nomes longo:, " , longos)