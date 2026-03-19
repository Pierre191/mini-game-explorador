# Mini Jogo: Explorador de Mapas (com paredes + armadilhas + tesouro escondido)

# Configurações do Mapa
LARGURA = 10
ALTURA = 5

# Tesouro (escondido: não desenha no mapa)
tesouro = {"x": 8, "y": 3}

# Armadilhas (posições que causam game over)
armadilhas = {
	(1, 3),
	(7, 1),
}

# Paredes (obstáculos que bloqueiam movimento)
paredes = {
	(2, 0), (2, 1), (2, 2),
	(5, 2), (6, 2), (7, 2),
	(4, 4), (5, 4),
}

passos = 0

# Jogador
player = {"nome": "Explorador", "x": 0, "y": 0}

def desenhar_mapa():
	print("\n" * 2)
	for y in range(ALTURA):
		linha = ""
		for x in range(LARGURA):
			if (x, y) == (player["x"], player["y"]):
				linha += "👤"
			elif (x, y) in paredes:
				linha += "⬛"
			# Armadilha escondida: não desenha nada
			# elif (x, y) in armadilhas:
			# 	linha += "🕳️"
			# Tesouro escondido: não desenha nada
			# elif (x, y) == (tesouro["x"], tesouro["y"]):
			# 	linha += "💎"
			else:
				linha += "🟩"
		print(linha)

def pode_andar_para(novo_x, novo_y):
	# bordas
	if novo_x < 0 or novo_x >= LARGURA or novo_y < 0 or novo_y >= ALTURA:
		return False
	# paredes
	if (novo_x, novo_y) in paredes:
		return False
	return True

print(f"Bem-vindo, {player['nome']}! Use W, A, S, D para se mover (ou Q para sair).")

while True:
	desenhar_mapa()
	comando = input("Movimento: ").lower().strip()

	# Calcula a próxima posição
	nx, ny = player["x"], player["y"]

	if comando == "w":
		ny -= 1
	elif comando == "s":
		ny += 1
	elif comando == "a":
		nx -= 1
	elif comando == "d":
		nx += 1
	elif comando == "q":
		print("Saindo do jogo... Até mais!")
		break
	else:
		print("Comando inválido. Use W A S D ou Q.")
		continue

	# Move se puder
	if pode_andar_para(nx, ny):
		player["x"], player["y"] = nx, ny
		passos += 1
	else:
		print("🚫 Movimento bloqueado (parede ou borda).")
		continue

	# Game over (armadilha)
	if (player["x"], player["y"]) in armadilhas:
		desenhar_mapa()
		print(f"💥 Você caiu em uma armadilha em {passos} passos. GAME OVER!")
		break

	# Vitória (tesouro)
	if player["x"] == tesouro["x"] and player["y"] == tesouro["y"]:
		desenhar_mapa()
		print(f"🎉 Você encontrou o tesouro em {passos} passos!")
		break
