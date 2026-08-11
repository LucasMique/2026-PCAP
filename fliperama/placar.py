# =============================================================
# ARQUIVO    : placar.py (pasta fliperama)
# Conceitos  : Arquivo de texto, modo de abertura, write, close
# =============================================================

ARQUIVO = 'placar.csv'
NOMES = ['Advinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar']


def salvar_placar(vezes):
    # 'w' esvazia o arquivo e escreve tudo de novo.
    arquivo = open(ARQUIVO, 'w')
    for i in range(3):
        arquivo.write(NOMES[i] + ',' + str(vezes[i]) + '\n')
    arquivo.close()