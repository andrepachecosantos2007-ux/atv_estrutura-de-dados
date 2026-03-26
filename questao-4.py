def traduzir(lista):
    alfabeto = [" ", "a", "b", "c", "d", "e", "f", "g",
                "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    
    resultado = ""
    
    for num in lista:
        resultado += alfabeto[num]
    
    return resultado

print(traduzir([2,15,13,0,4,9,1]))