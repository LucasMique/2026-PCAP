# =============================================================
# Disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
# Projeto    : Jogo "Pedra-Papel-Testoura"
# Arquivo    : ppt;py
# Autor      : Lucas Klipan Miquelin
# Data       : 16/06/2026
# =============================================================

import random

# Base herdada da v1: as três opções e o sorteio da máquina
opcoes = ["pedra", "papel", "tesoura"]
jogada_maquina = random.choice(opcoes)

# Lemos a jogada e NORMALIZAMOs o texto (deixar igual para poder comparar)
entrada = input("Sua jogada(pedra, papel ou tesoura): ")
jogada_jogador = entrada.lower().strip() # tudo minúsculo e sem espaços nas pontas

# Validação: a jogada digitada está entre as opções válidas?
if jogada_jogador not in opcoes:
    print("Jogada inválida! Digite pedra, papel ou tesoura.")
else:
    # Texto limpo e válido: agora é seguro motrar as duas jogadas
    print("Você jogou:", jogada_jogador)
    print("A máquina jogou:", jogada_maquina)