'''
problema: beecrowd | 1006
Data: 2026.04.09
Estudante: Lucas Klipan Miquelin
'''
# objetivo: ler 3 valores, calcular a média deles, sabendo o peso de cada 1, sabendo que tambêm cada nota pode ter 1 casa decimal.

# --- análise (liac) ---
# Entrada: três notas com peso 2, 3, e 5, respectivamente.
# processamento: (A * 2 + B * 3 + C * 5) / 10
# saída: exibir no formato "MEDIA = resultado" com 1 casa decimal.

A = float(input())
B = float(input())
C = float(input())

media = (A * 2 + B * 3 + C * 5) / 10

print(f"MEDIA = {media:.1f}")