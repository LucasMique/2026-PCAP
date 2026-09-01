# =========================================
# Arquivo: modulos.py
# Disciplina: 2026-PCAP
# Aula: 20
# Autor: Lucas Klipan Miquelin
# Data: 2026.08.04
# Conceitos: 
# =========================================

def ler_opcao(mensagem, validas):
    resposta = input(mensagem + ':  ').strip()
    while resposta not in validas:
        print("Opção inválida, tente novamente.")
        resposta = input(mensagem + ":   ").strip()
    return resposta

def ler_numero(mensagem, minimo, maximo):
    numeros = []
    for n in range(minimo, maximo + 1):
        numeros.append(str(n))
    return int(ler_opcao(mensagem, numeros))


def ler_texto(mensagem):
    # So devolve quando o texto nao estiverr vasio.
    resposta = input(mensagem + ': ').strip()
    while resposta == '':
        print('Nao pode ficar em branco! Tente de novo.')
        resposta = input(mensagem + ': ').strip()
    return resposta