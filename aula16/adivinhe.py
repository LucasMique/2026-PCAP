# =============================================================
# Disciplina : Pensamento Computacional, Algorítimos e Programação (PCAP)
# Projeto    : Jogo "Adivinhe o Número"
# Arquivo    : Adivinhe.py
# Autor      : Lucas Klipan Miquelin
# Data       : 28/05/2026
# =============================================================

import random


# Esses são os códigos dos segredos. caso usados, irão fazer uma mensagem especial. Ou, até, um cheat para você ganhar imediatamente.
baaa = 1000

resenhéx =  67

numerofavorito = 777

aresenhanaopara = 999

nope = 666

ganhei = 676767077707

# === Sub-rotina: o jogo inteiro vira uma função reutilizável ===
def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou = False

    while chances > 0 and not acertou:
        palpite = int(input("Seu palpite (1 a " + str(maximo) + "): "))

        if palpite == numero_secreto:
            print("🎊 Acertou!")
            acertou = True
        elif palpite == resenhéx:
            print("bandido quer 67 resenha bandido quer 67 resenha")
        elif palpite == nope:
            print("👹")
        elif palpite == numerofavorito:
            print("haha esse é meu número favorito! é perfeito.")
        elif palpite == aresenhanaopara:
            print("esse número é maligno. tão perto de 1000 mas tão longe....")
        elif palpite == baaa:
            print("Essa é a tropa das ovelhas! Aqui só há ovelhas e resenha. 🐑🐑🐑🐑 Bááááá 🐑🐑🐑🐑")
        elif palpite == ganhei:
            print("Oloko seu xiter horrível ganhou xitando lirili larilá orcalero orcalá tung tung tung sahurr")
            acertou = True
        elif palpite < numero_secreto:
            print("📈 Muito baixo!")
        else:
            print("📉 Muito alto!")

        chances = chances - 1
        print("Chances restantes:", chances)
        
    return acertou

# === Níveis guardados em uma lista de listas: [nome, maximo, chances] ===
niveis = [
    ["Fácil", 10, 3],
    ["Médio", 100, 5],
    ["Impossível", 1000, 10],
]

# === Menu de escolha do nível ===
print(" Escolha o nível de difficuldade:")
print("1 - Fácil (1 a 10, 3 chances)")
print("2 - Médio (1 a 100, 5 chances)")
print("3, Impossível (1 a 1000, 10 chances)")
print("Você consegue encontrar todos os segredos nesse jogo?")
opcao = int(input("Digite 1, 2, ou 3:"))

# A opção 1 está na posição 0 da lista, por isso o ajuste
nivel = niveis[opcao - 1]

# === Iniciamos o jogo com a configuração do nível escolhido ===
print("Você escolheu o nível:", nivel[0])
venceu = jogar(nivel[1], nivel[2])

if not venceu:
    print("💀 Fim de jogo! Tente um nível mais fácil. 😜 ")
