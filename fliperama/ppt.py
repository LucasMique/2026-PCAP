# ============================================================================================================
# ARQUIVO      : ppt.py (Pasta fliperama)
# Conceitos    : Jogo como módulo, lista como tabela de nomes, função com retorno, operador % para dar a volta
# Base         : Jogo da aula 17 (Atividade 11)
# Autor        : Lucas Klipan Miquelin
# Data         : 2026.08.11
# ============================================================================================================

# Importa função randint que gera um número aleatório
from random import randint

# Importa as funções título e linha do arquivo telas.py
from telas import titulo, linha

# Importa a função ler_opcao que valida a entrada do usuário do arquivo módulos.py
from modulos import ler_opcao

# Lista com PEDRA == posição 0 ; PAPEL == posição 1 e TESOURA == 2
JOGADAS = ['PEDRA', 'PAPEL', 'TESOURA']

def quem_vence(jogador, computador):
    if jogador == computador:
        return 'empate'
    if jogador == (computador + 1) % 3:
        return 'jogador' 
    return 'computador'


# Motra as opcões de jogo
def mostrar_jogadas():
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] Tesoura')
    linha()

def jogar_ppt():
    titulo('PEDRA - PAPEL - TESOURA')

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao('Sua jogada', ['0', '1', '2']))
        computador = randint(0, 2)

        print('Você jogou ' + JOGADAS[jogador])
        print('Computador jogou ' + JOGADAS[computador])

        resultado = quem_vence(jogador, computador)

        if resultado == 'empate':
            print('Empate! Ninguém venceu!')
        elif resultado == 'jogador':
            pontos_jogador += 1
            print('Você venceu essa rodada!')
        elif resultado == 'computador':
            pontos_computador += 1
            print('Computador venceu essa rodada')

        linha()
        print(f'Placar: Jogador + {pontos_jogador} X {pontos_computador} computador ')
        linha()

    if pontos_jogador > pontos_computador:
        titulo('YOU WIN')
    else: 
        titulo('YOU LOSE')