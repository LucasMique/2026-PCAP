# =============================================================
# Disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
# Projeto    : Jogo "Pedra-Papel-Testoura"
# Arquivo    : ppt;py
# Autor      : Lucas Klipan Miquelin
# Data       : 16/06/2026
# =============================================================

import random

# === Sub-rotina: decide o resultado de UMA rodada e devolve um texto ===
def resultado(jogador, maquina):
    # Testa caso a caso; o primeiro return q bater já encerra a função
    if jogador == maquina:
        return "empate"
    if jogador == "pedra" and maquina == "tesoura":
        return "jogador"
    if jogador == "papel" and maquina == "pedra":
        return "jogador"
    if jogador == "tesoura" and maquina == "papel":
        return "jogador"
    if jogador == "pedra" and maquina == "lagarto":
        return "jogador"
    if jogador == "lagarto" and maquina == "spock":
        return "jogador"
    if jogador == "spock" and maquina == "tesoura":
        return "jogador"
    if jogador == "tesoura" and maquina == "lagarto":
        return "jogador"
    if jogador == "lagarto" and maquina == "papel":
        return "jogador"
    if jogador == "papel" and maquina == "spock":
        return "jogador"
    if jogador == "spock" and maquina == "pedra":
        return "jogador"
    return "maquina"

# === opções de jogadas ===
opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]

# Variável que decide se o jogo acontece ou não; no final se decide se repete ou não.
jogar_dnv = "sim"

# Enquanto a variável jogar_dnv estiver em "sim", o jogo irá acontecer.
while jogar_dnv == "sim":
    pontos_jogador = 0
    pontos_maquina = 0
    for rodada in range(1, 6):
        print("--- Rodada", rodada, "---")
        jogada_maquina = random.choice(opcoes)
        # Leitura enxtuta: ler + .lower() + .strip() em uma linha só
        jogada_jogador = input("Sua jogada: ").lower().strip()
    
        if jogada_jogador not in opcoes:
            print("Inválida! Você perde a rodada.")
            pontos_maquina = pontos_maquina + 1
        else:
            quem = resultado(jogada_jogador, jogada_maquina)  # chamamos a subrotina
            if quem == "empate":
                print("Empate!")
            elif quem == "jogador":
                print("Você ganhou a rodada!")
                pontos_jogador = pontos_jogador + 1
            else:
                print("A máquina ganhou a rodada!")
                pontos_maquina = pontos_maquina + 1
    print("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)
    jogar_dnv = input("Jogar de novo?(sim ou não): ").lower().strip() # Aqui é feita a escolha entre continuar jogando ou apenas parar.