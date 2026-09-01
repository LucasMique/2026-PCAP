# ============================================================================================================
# ARQUIVO      : caraoucoroa.py (Pasta fliperama) (jogo autoritário)
# Conceitos    : def, %, randint, linha, titulo
# Autor        : Lucas Klipan Miquelin
# Data         : 2026.08.11
# ============================================================================================================

from random import randint
from modulos import ler_opcao
from telas import titulo, linha

# As duas jogadas do cara ou coroa.
CARAOUCOROA = ['CARA', 'COROA']

# Demonstra as duas possibilidades de jogada, o famoso cara ou coroa.
def mostrar_possibilidades_de_jogada():
    print('[0] Cara')
    print('[1] Coroa')

# Aqui que começa a jogatina.
def jogar_caraoucoroa():
    titulo('CARA OU COROA')

    pontos_jogador_coc = 0
    pontos_computador_coc = 0

    while pontos_jogador_coc < 2 and pontos_computador_coc < 2:
        mostrar_possibilidades_de_jogada()

        # Usa-se ler opção aqui já que "Cara" e "Coroa" sao ambos palavras, não números.
        # Também é mais conveniente digitar números do que a palavra inteira.
        jogador_coc = int(ler_opcao('Sua jogada', ['0', '1']))
        # O Computador escolhe se é cara ou coroa.
        computador_coc = randint(1, 1000)
        # E esse é o cálculo que faz isso verdade.
        resultado_coc = computador_coc % 2

        if resultado_coc == 0:
            amoedacaiu = "CARA"
        else:
            amoedacaiu = "COROA"

        # Os dois prints, detalhando o que acontece na partida.
        print('VOCÊ SELECIONOU ' + CARAOUCOROA[jogador_coc])
        print('A MOEDA CAIU, E SEU RESULTADO FOI ' + amoedacaiu )

        linha()

        # As linhas de IF, determinando caso você ganhou ou perdeu.
        if resultado_coc == jogador_coc:
            print("Você acertou!")
            pontos_jogador_coc += 1
        elif resultado_coc is not jogador_coc:
            print("Você errou!")
            pontos_computador_coc += 1

        # O placar, que aparece após toda jogada.
        linha()
        print(f'Placar: Jogador {pontos_jogador_coc} X {pontos_computador_coc} computador ')

    # O resultado da partida.
    if pontos_jogador_coc > pontos_computador_coc:
        titulo("VOCÊ VENCEU!")
    else:
        titulo('VOCÊ PERDEU..')