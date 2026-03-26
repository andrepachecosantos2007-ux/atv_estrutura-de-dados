import random

cartela = []

numeros = list(range(100))  
random.shuffle(numeros)     

indice = 0

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(numeros[indice])
        indice += 1
    cartela.append(linha)
for linha in cartela:
    print(linha)