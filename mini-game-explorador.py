# Mini Jogo: Explorador de Mapas
# Objetivo: Praticar lógica de matrizes, coordenadas (X, Y) e manipulação de dicionários.

# Configurações do Mapa
LARGURA = 10
ALTURA = 5

# Jogador (Representado por um Dicionário)
player = {
    "nome": "Explorador",
    "x": 0,
    "y": 0
}

def desenhar_mapa():
    print("\n" * 2) # Limpa um pouco o terminal
    for y in range(ALTURA):
        linha = ""
        for x in range(LARGURA):
            if player["x"] == x and player["y"] == y:
                linha += "👤" # Emoji de jogador
            else:
                linha += "🟩" # Grama
        print(linha)

# Loop Principal do Jogo
print(f"Bem-vindo, {player['nome']}! Use W, A, S, D para se mover (ou Q para sair).")

while True:
    desenhar_mapa()
    comando = input("Movimento: ").lower()

    if comando == 'w' and player["y"] > 0: # Cima
        player["y"] -= 1
    elif comando == 's' and player["y"] < ALTURA - 1: # Baixo
        player["y"] += 1
    elif comando == 'a' and player["x"] > 0: # Esquerda
        player["x"] -= 1
    elif comando == 'd' and player["x"] < LARGURA - 1: # Direita
        player["x"] += 1
    elif comando == 'q':
        print("Saindo do jogo... Até mais!")
        break
