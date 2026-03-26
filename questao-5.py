matriz = [
    [8, 0, 7],
    [4, 5, 6],
    [3, 10, 2]
]
def eh_magico(matriz):
    soma = sum(matriz[0])
    
    for linha in matriz:
        if sum(linha) != soma:
            return False
    
    for i in range(len(matriz)):
        coluna = matriz[0][i] + matriz[1][i] + matriz[2][i]
        if coluna != soma:
            return False
    
    diag1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
    diag2 = matriz[0][2] + matriz[1][1] + matriz[2][0]
    
    if diag1 != soma or diag2 != soma:
        return False
    
    return True



print(eh_magico(matriz))