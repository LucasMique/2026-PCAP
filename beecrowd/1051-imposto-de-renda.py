'''
problema: beecrowd | 1051
data: 2026.04.30
Estudante: lucas klipan miquelin
'''
# Objetivo: Impostar certas quantidades de dinheiro, conforme o exercício ditou.

# --- ANÁLISE (LIAC) ---

#entrada: Número com float de 2 dígitos
#processamento: cálculos de porcentagem utilizando multipliação, junto com o fato de adicionar as classes de dinheiro já impostadas.
#saída: o quanto de dinheiro precisa ser pago de imposto

# entrada
dindin = float(input())
# processamento E saída
if dindin < 2000.00:
    print("Isento")
elif 2000.01 <= dindin < 3000.02:
    dindin = (dindin - 2000) * 0.08
    print(f"R$ {dindin:.2f}")
elif 3000.01 < dindin < 4500.02:
    dindin = ((1000 * 0.08) + ((dindin - 3000) * 0.18))
    print(f"R$ {dindin:.2f}")
elif 4500.01 < dindin:
    dindin = ((1000 * 0.08) + (1500 * 0.18) + ((dindin - 4500) * 0.28))
    print(f"R$ {dindin:.2f}")
