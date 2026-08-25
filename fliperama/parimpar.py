# ============================================================================================================
# ARQUIVO      : parimpar.py (Pasta fliperama)
# Conceitos    : def, randint, for, def 
# Base         : Jogo da aula 17 (Atividade 11)
# Autor        : Lucas Klipan Miquelin
# Data         : 2026.08.11
# ============================================================================================================


from random import randint
from telas import titulo, linha
from modulos import ler_numero, ler_opcao

def resultado(jogador_troll, maquina_troll):
    if (jogador_troll + maquina_troll) % 2 == 0:
        return "par"
    if (jogador_troll + maquina_troll) % 2 == 1:
        return "impar"


def jogar_parimpar():
    titulo('PAR OU IMPAR')
    
    pontos_jogador_troll = 0
    pontos_maquina_troll = 0
    for rodada in range(1, 6):
        print("--- Rodada", rodada, "---")
        maquina_troll = int(randint(0, 5))
        jogador_tenebroso = ler_opcao('Par ou Impar?', ['par', 'impar']).lower().split()
        jogador_troll = ler_numero("Digite seu palpite", 1, 5)
        retorno = resultado(jogador_troll, maquina_troll)
        print("Jogada da máquina:", maquina_troll)   
        if retorno == jogador_tenebroso:
            print("Você ganhou!")
            linha()
            pontos_jogador_troll = pontos_jogador_troll + 1
        else:
            print("Você perdeu.")
            linha()
            pontos_maquina_troll = pontos_maquina_troll + 1
    linha()
    print("Placar -> Você:", pontos_jogador_troll, "| Máquina:", pontos_maquina_troll)
    linha()