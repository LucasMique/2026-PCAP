# =============================================================
# Disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
# Projeto    : Jogo "Pedra-Papel-Testoura"
# Arquivo    : ppt;py
# Autor      : Lucas Klipan Miquelin
# Data       : 16/06/2026
# =============================================================

import random

# 1) As três jogadas possíveis, guardadas como TEXTO (strings) numa lista
opcoes = ["pedra", "papel", "tesoura"]

# 2) O computador sorteia uma jogada de dentro da lista
jogada_maquina = random.choice(opcoes)

# 3) Pedimos a jogada do jogador (input SEMPRE devolve texto)
jogada_jogador = input("Sua jogada (pedra, papel, ou tesoura:) ")

# 4) Mostramos as duas jogadas deste primeiro teste
print("Você jogou:", jogada_jogador)
print("A máquina jogou:", jogada_maquina)