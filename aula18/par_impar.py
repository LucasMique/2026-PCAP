# ════════════════════════════════════════════════════════════
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Lucas Klipan Miquelin
# Data       : 25/06/2026
# ════════════════════════════════════════════════════════════

import random

opcoes = ["par", "impar"]
pontos_jogador_troll = 0
pontos_maquina_troll = 0
# Variável que decide se o jogo acontece ou não; no final se decide se repete ou não.
jogar_dnv = "sim"

# Váriavel que escolhe a difficuldade. Pode parecer estranho, mais quanto mais números mais difficuldade, já que a chance de cair um número par é menor em relação á de impar, e vice versa.
numero_escolhido = int(input("Difficuldade: Escolha até que número a ia pode escolher: "))

def resultado(jogador_troll, maquina_troll):
    if (jogador_troll + maquina_troll) % 2 == 0:
        return "par"
    if (jogador_troll + maquina_troll) % 2 == 1:
        return "impar"

# Enquanto a variável jogar_dnv estiver em "sim", o jogo irá acontecer.
while jogar_dnv == "sim":
    numero_escolhido = int(input("Difficuldade: Escolha até que número a ia pode escolher: "))
    pontos_jogador_troll = 0
    pontos_maquina_troll = 0
    for rodada in range(1, 6):
        print("--- Rodada", rodada, "---")
        maquina_troll = int(random.randint(0, numero_escolhido))
        jogador_tenebroso = input("Par ou impar?: ").lower().strip()
        jogador_troll = int(input("Seu palpite (0 a 5): "))
        retorno = resultado(jogador_troll, maquina_troll)
        if jogador_tenebroso not in opcoes:
            print("Escolha PAR ou IMPAR.")
            pontos_maquina_troll = pontos_maquina_troll + 1
        elif jogador_troll > 5:
            print("Número de 0 a 5. Não sabe ler?")
            pontos_maquina_troll = pontos_maquina_troll + 1
        elif retorno == jogador_tenebroso:
            print("Você ganhou!")
            pontos_jogador_troll = pontos_jogador_troll + 1
        else:
            print("Você perdeu.")
            pontos_maquina_troll = pontos_maquina_troll + 1
    print("Placar -> Você:", pontos_jogador_troll, "| Máquina:", pontos_maquina_troll)
    jogar_dnv = input("Jogar de novo?(sim ou não)(com a mesma difficuldade): ").lower().strip() # Jogar denovo sem fechar o programa? Aqui pode!