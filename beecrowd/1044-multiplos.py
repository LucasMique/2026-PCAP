'''
problema: becrowd | 1044
data: 2026.04.16
estudante: Lucas Klipan Miquelin
'''
# Objetivo: verificar se dois inteiros são multiplos entre si

# --- análise (liac) ---
# entrada: dois inteiros A e B na mesma linha separados por espaço
# Processamento> identificar maior e menor, verificar se maior % menor == 0
# saída: "Sao multiplos" ou "Nao sao multiplos"

A, B = input().split()
A = int(A)
B = int(B)

# identifica maior e menor para aplicar o operador % corretamente
# (o resto sempre deve ser calculado dividindo o maior pelo menor)
if A > B:
    maior = A
    menor = B
else: 
    maior = B
    menor = A

# Operador % (módulo): retorna o resto da divisão inteira
# se o resto for 0, o maior é multiplo do menor, logo são multiplos entre si
if maior % menor == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
    