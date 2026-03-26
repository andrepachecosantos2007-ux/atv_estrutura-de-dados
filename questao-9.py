# Primeiro eu monto o tabuleiro igual ao exemplo da imagem
# -1 sou eu, 1 é o oponente e 0 é o lugar vazio
tabuleiro = [
    [-1,  1,  1],
    [-1, -1,  0],
    [ 0,  1,  0]
]

# Variáveis para marcar se achei um lugar e onde ele está
achou_vazio = False
linha_vazia = -1
coluna_vazia = -1

# Vou usar dois "for" para varrer a matriz toda (linha por linha)
for l in range(3):
    for c in range(3):
        # Se eu encontrar um 0, quer dizer que achei um lugar para jogar!
        if tabuleiro[l][c] == 0:
            linha_vazia = l
            coluna_vazia = c
            achou_vazio = True
            break # Achei um? Já posso parar de procurar na linha
    
    if achou_vazio == True:
        break # Se já achei, paro de procurar no tabuleiro todo

# Agora mostro o resultado na tela
print("--- ANALISANDO O JOGO DA VELHA ---")

if achou_vazio == True:
    print(f"Encontrei um espaço livre!")
    print(f"Sugestao de jogada: Linha {linha_vazia} e Coluna {coluna_vazia}")
else:
    print("Vish, o tabuleiro ja esta cheio! Nao tem onde jogar.")