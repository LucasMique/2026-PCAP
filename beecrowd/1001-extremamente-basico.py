'''
problema: beecrowd | 1001
data: 2026.04.07
estudante: Lucas Klipan Miquelin
'''
# Objetivo: Ler dois inteiros nas variáveis A e B, calcular a soma em X e exibir o resultado.

# --- ANÁLISE (LIAC) ---
# entrada: dois números inteiros, cada um em uma linha separada
# processamento: somar A + B e armazenar em X
# saída: Exibir no formato "X = valor" (espaços ao redor do=, sem mensagens extras)

# int()       -> converte o texto lido para número inteiro
# input()     -> lê o valor fornecido (digitado ou pelo Beecrowd)
# int(input())-> lê e converte em uma única instrução
A = int(input())
B = int(input())

# O enunciado especifica explicitamente as variáveis A,B,X, - seguir à risca
X = A + B

#f-string: insere o valor de X dentro do texto com {}
#Atenção: espaço antes e depois do = é obrigatório onforme o enunciado
print(f"X = {X}")
