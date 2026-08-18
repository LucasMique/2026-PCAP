# =========================================
# Arquivo: main.py
# Disciplina: 2026-PCAP
# Aula: 20
# Autor: Lucas Klipan Miquelin
# Data: 2026.08.04
# Conceitos: 
# =========================================

# Importar funçoes de arquivos (módulos)
from telas import titulo, linha
from advinhe import jogar_advinhe
from ppt import jogar_ppt
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores

NOME_DO_DONO = "lucas"
OPCOES = ["0", "1", "2", "3"]
NOMES_DOS_JOGOS = ['Advinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar']
vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()

def mostrar_placar():
    titulo('PLACAR')
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')

while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('[0- Sair do fliperama')
    print('[1] - Jogo advinhe o número')
    print('[2] - Pedra-Papel-Tesoura')
    print('[3] - Jogadores')
    linha()
    opcao = ler_opcao("Escolha uma opção", OPCOES)

    if opcao == "0":
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        print("Até a Próxima!")
        break
    if opcao == '3':
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) - 1
        vezes_jogado[indice] = vezes_jogado[indice] + 1

        if opcao == '1':
            jogar_advinhe
        else:
            jogar_ppt()

    input('Pressione Enter para voltar ao menu...')
