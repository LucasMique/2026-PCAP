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
from placar import salvar_placar


NOME_DO_DONO = "lucas"
OPCOES = ["0", "1", "2"]
NOMES_DOS_JOGOS = ['Advinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar']
vezes_jogado = [0, 0, 0]

def mostrar_placar():
    titulo('PLACAR')
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')

while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('0 - Sair do fliperama')
    print('1 - Jogo advinhe o número')
    print('2 - Pedra-Papel-Tesoura')
    linha()
    opcao = ler_opcao("Escolha uma opção", OPCOES)

    if opcao == "0":
        mostrar_placar()
        salvar_placar(vezes_jogado)
        print("Até a Próxima!")
        break
    elif opcao == "1":
        jogar_advinhe()
    elif opcao == "2":
         jogar_ppt()

    indice = int(opcao) - 1
    vezes_jogado[indice] = vezes_jogado[indice] + 1