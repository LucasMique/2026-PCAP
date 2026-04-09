'''
problema: beecrowd | 1008
data: 2026.04.09
estudante: Lucas Klipan Miquelin
'''
# Objetivo: Calcular sálario utilizando número de horas trabalhadas, seu número e seu valor ganho por hora.

# --- análise (liac) ---
# entrada: Número, horas trabalhadas e valor ganho por hora
# processamento: Multiplicação de valor ganho por hora e horas. com float de 2 casas
# saída: número e salário com dois números de float.

# leitura das entradas: - observe o enunciado: Quantas variáveis e de qual tipo?
N = input()
H = int(input())
V = float(input())

# calcule o salário - use o 1009 como referência de estrutura
SAL = H * V

# saída - observe o formato exato e o número de casas decimais no enunciado
print(f"NUMBER = {N}")
print(f"SALARY = U$ {SAL:.2f}")