'''
problema: beecrowd | 1002
Data: 2026.04.07
Estudante: Lucas Klipan Miquelin
'''
# Objetivo: Calcular a área de um círculo usando a fórmula e um número de ráio flutuante

# --- ANÁLISE (LIAC) ---
# Entrada: medida do ráio
# Processamento: cálculo usando a fórmula de área de um círculo
# Saída: a area do círculo

# Leitura do raio como número decimal
R = float(input())

# Defina pi onforme o enunciado indica
pi = 3.14159

# qual é a fórmula da área do círculo?
AREA =  (R ** 2) * pi

# Saída - observe o formato exato e o número de casas decimais no enunciado
print(f"A={AREA:.4f}")
