# =============================================================
# Disciplina : Pensamento Computacional, Algorítimos e Programação (PCAP)
# Projeto    : Jogo "Adivinhe o Número"
# Arquivo    : Adivinhe.py
# Autor      : Lucas Klipan Miquelin
# Data       : 28/05/2026
# =============================================================

import random


# 1) Sorteamos o número secreto entre 1 e 10
numero_secreto = random.randint(1, 10)
chances = 3
acertou = False


# 2) Pedimos um palpite (Input devole texto; convertemos para inteiro)
while chances > 0 and not acertou:
    palpite = int(input("Digite um número de 1 a 10: "))

    if palpite == numero_secreto:
        print("🎊 Acertou! O número era", numero_secreto)
        acertou = True
    elif palpite < numero_secreto:
        print("📈 Muito baixo! Tente um número maior.")
    else:
        print("📉 Muito alto! Tente um número menor.")

chances = chances - 1 # gasta uma chance
print("Chances restantes:", chances)