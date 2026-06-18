# =============================================================
# Disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
# Projeto    : Jogo "Pedra-Papel-Testoura"
# Arquivo    : ppt;py
# Autor      : Lucas Klipan Miquelin
# Data       : 16/06/2026
# =============================================================

import random

opcoes = ["pedra", "papel", "tesoura"]

# Placar das duas partes
pontos_jogador = 0
pontos_maquina = 0

# Jogamos 5 rodadas usando repetição (range vai de 1 até o número ANTERIOR ao limite)
for rodada in range(1, 6):
    print("--- Rodada", rodada, "---")
    # A cada volta do laço: novo sorteio e nova leitura (igual à v3)
    jogada_maquina = random.choice(opcoes)
    entrada = input("Sua jogada(pedra, papel ou tesoura): ")
    jogada_jogador = entrada.lower().strip()

    # Mesmas regras da v3 - só que agora cada resultado vale PONTO
    if jogada_jogador not in opcoes:
        print("Inválida! Você perde a rodada.")
        pontos_maquina = pontos_maquina + 1
    elif jogada_jogador == jogada_maquina:
        print("Empate!")
    elif jogada_jogador == "pedra" and jogada_maquina == "tesoura":
        print("Você ganhou a rodada!")
        pontos_jogador = pontos_jogador + 1
    elif jogada_jogador == "papel" and jogada_maquina == "pedra":
        print("Você ganhou a rodada!")
        pontos_jogador = pontos_jogador + 1
    elif jogada_jogador == "tesoura" and jogada_maquina == "papel":
        print("Você ganhou a rodada!")
        pontos_jogador = pontos_jogador + 1
    else:    # não caiu em nenhuma vitória acima -> sobra a máquina
        print(" A maquina venceu! ela jogou", jogada_maquina)
        pontos_maquina = pontos_maquina + 1

# Placar final, depois das 5 rodadas
print("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)