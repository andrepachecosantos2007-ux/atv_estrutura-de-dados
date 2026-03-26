# Primeiro eu criei a matriz com os números que estavam na imagem
# Cada linha é uma cidade, de 0 até 4
distancias = [
    [0, 15, 30, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 3, 11],
    [5, 17, 3, 0, 80],
    [12, 28, 11, 80, 0]
]

# --- PARTE A (Só uma consulta rápida) ---
print("--- TESTE DE DISTANCIA ---")

# Peço para o usuário digitar os números das cidades
de_onde = int(input("Cidade de partida (0-4): "))
para_onde = int(input("Cidade de destino (0-4): "))

# Aqui eu busco na tabela: o primeiro [ ] é a linha, o segundo [ ] é a coluna
resultado = distancias[de_onde][para_onde]

print("A distancia entre elas eh:", resultado, "km")
print("--------------------------")


# --- PARTE B (Somar vários caminhos) ---
print("--- CALCULANDO UM PERCURSO INTEIRO ---")

# Essa variável começa em zero para ir guardando a soma
total = 0

# A professora pediu até 6 vezes, então uso o for
for i in range(6):
    print("Vamos ver o trecho", i + 1)
    
    # Pergunto as cidades do trecho atual
    cid1 = int(input("  Sair de: "))
    cid2 = int(input("  Chegar em: "))
    
    # Pego o valor na matriz e somo no que eu já tinha guardado
    valor_do_trecho = distancias[cid1][cid2]
    total = total + valor_do_trecho
    
    # Se a pessoa não quiser fazer os 6 trechos, ela pode parar antes
    parar = input("  Quer parar por aqui? (s/n): ")
    if parar == "s":
        break

# No final, mostro quanto deu a conta toda
print("--------------------------")
print("O total que voce percorreu foi:", total, "km")