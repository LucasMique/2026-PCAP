'''
problema: beecrowd | 1037
data: 2026.04.16
estudante: Lucas Klipan Miquelin
'''
# Objetivo: ler quatro inteiros A, B, C e D na mesma linha. Se B > C e D > A e C+D > A+B e C e D forem positivos e A for par, escreva "Valores aceitos"; senão, "Valores nao aceitos".

# --- análise (liac) ---
# entrada: 4 números inteiros
# Processamento: Ver se caso B > C, D > A, C+D > A+B, C e D forem positivos, e A for par. Se tudo vor verdadeiro, escrever "valores aceitos". caso contrário, "Valores não aceitos"
# saída:  "Valores nao aceitos" ou "Valores aceitos"

A,B,C,D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if B > C and D > A and (C+D) > (A+B) and C > 0 and D > 0 and (A % 2 == 0):    
 print("Valores aceitos")
else:
 print("Valores nao aceitos")