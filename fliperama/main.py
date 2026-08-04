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
from modulos import ler_opcao

NOME_DO_DONO = "lucas"
OPCOES - ["0", "1"]

while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('1 - Jogo advinhe o número')
    print('0 - Sair do fliperama')
    linha()
    opcao = ler_opcao("Escolha uma opção", OPCOES)

    if opcao == "0":
        print("Até a Próxima!")
        break
    elif opcao == "1":
        jogar_advinhe()