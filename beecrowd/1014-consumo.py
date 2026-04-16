'''
problema: beecrowd | 1014
data: 2026.04.16
estudante: Lucas Klipan Miquelin
'''
# Objetivo: Calcular o consumo médio de um automóvel em km/l

# --- análise (liac) ---
# entrada: distância total percorrida e o total de combustível gasto
# processamento: consumo = km/l
# saída: Consumo com 3 casas decimais seguido de km/l

# Lê a distancia total percorrida em km (tipo inteiro)
X = int(input())

# Lê o total de combustível gasto em litros (tipo ponto flutuante)
Y = float(input())

# calcula o consumo médio: km dividido por L
consumo = X / Y

# Exibe o resultado com 3 casas decimais e a unidade km/l
print(f"{consumo:.03f} km/l")