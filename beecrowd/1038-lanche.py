'''
problema | beecrowd 1038
data: 2026.04.23
estudante: Lucas KlipaN Miquelin
'''
# Objetivo: entre valores já estabelecidos, resultar o total de 2 escolhidos

# --- Análise (liac) ---
# entrada: 2 códigos equivalentes á 2 itens no menu.
# processamento: pegar o valor de cada item dos códigos e somar.
# saída: total, r$ e o valor.

# entrada
A, B = input().split()

# processamento
if A % 2 is 0:
    A = 