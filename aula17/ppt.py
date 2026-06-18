# =============================================================
# Disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
# Projeto    : Jogo "Pedra-Papel-Testoura"
# Arquivo    : ppt;py
# Autor      : Lucas Klipan Miquelin
# Data       : 16/06/2026
# =============================================================

import random

# Tudo isto já vem pronto da v1 e v2: sortear, ler e limpar a jogada
opcoes = ["pedra", "papel", "tesoura"]
jogada_maquina = random.choice(opcoes)

entrada = input("Sua jogada(pedra, papel ou tesoura): ")
jogada_jogador = entrada.lower().strip()
print("Você jogou:", jogada_jogador, "| Máquina:", jogada_maquina)

# Decidimos o resultado comparando as duas jogadas (textos)
# A ORDEM dos testes importa: primeiro inválida, segundo empate, depois as vitórias
if jogada_jogador not in opcoes:
    print("Jogada inválida! Digite pedra, papel, ou tesoura.")
elif jogada_jogador == jogada_maquina:
    print("Empate! os dois jogaram", jogada_maquina)
# as três (e únicas) formas de o JOGADOR vencer - a regra clássica
elif jogada_jogador == "pedra" and jogada_maquina == "tesoura":
    print("Você venceu! Pedra quebra tesoura.")
elif jogada_jogador == "papel" and jogada_maquina == "pedra":
    print("Você venceu! Papel embrulha pedra.")
elif jogada_jogador == "tesoura" and jogada_maquina == "papel":
    print("Você venceu! Tesoura corta papel.")
else:    # não caiu em nenhuma vitória acima -> sobra a máquina
    print(" A maquina venceu! ela jogou", jogada_maquina)