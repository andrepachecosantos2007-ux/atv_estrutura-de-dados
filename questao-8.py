# --- PASSO 1: GUARDAR O GABARITO ---
# Vou criar uma lista vazia para colocar as 10 respostas certas
gabarito = []

print("Fase 1: Digite o gabarito da prova (a, b, c, d ou e)")
for i in range(10):
    letra = input(f"Resposta correta da questao {i+1}: ")
    gabarito.append(letra) # O append coloca a letra dentro da lista

print("-" * 30)

# --- PASSO 2: LER OS DADOS DOS 3 ALUNOS ---
# Uso outro for, mas agora para os 3 alunos
for aluno in range(3):
    print(f"\nDados do Aluno {aluno + 1}:")
    
    matricula = int(input("Digite a matricula (numero): "))
    
    respostas_aluno = [] # Lista para guardar o que esse aluno marcou
    nota = 0 # Toda prova começa com nota zero
    
    # Agora vou ler as 10 respostas que o aluno deu
    for j in range(10):
        resp = input(f"Resposta do aluno para a questao {j+1}: ")
        respostas_aluno.append(resp)
        
        # Aqui eu comparo: se o que ele respondeu for igual ao gabarito...
        if resp == gabarito[j]:
            nota = nota + 1 # ...ele ganha 1 ponto
            
    # Calculando os resultados finais
    percentual = (nota / 10) * 100
    
    # Mostrando tudo na tela
    print("\n--- RESULTADO FINAL ---")
    print("Matricula:", matricula)
    print("Respostas dadas:", respostas_aluno)
    print("Nota:", nota)
    print("Percentual de acerto:", percentual, "%")
    
    # Verificando se passou (media 7.0)
    if nota >= 7:
        print("Status: APROVADO")
    else:
        print("Status: REPROVADO")
    print("-" * 30)