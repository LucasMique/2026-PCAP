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

A = float(A)
B = float(B)

# processamento
if A == 1:
    A = 4.00
elif A == 2:
    A = 4.50
elif A == 3:
    A = 5.00
elif A == 4:
    A = 2.00
elif A == 5:
    A = 1.50

print (f"Total: R$ {A * B:.2f}")