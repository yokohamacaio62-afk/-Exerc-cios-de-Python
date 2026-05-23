lista = "PyThOn" 

maiusculas = []
minusculas = []

for letras in (lista):
    if letras.isupper(): 
        maiusculas.append(letras)
    else:  
        minusculas.append(letras)


print ("maiusculas:,", maiusculas)
print("minusculas:, ", minusculas)
