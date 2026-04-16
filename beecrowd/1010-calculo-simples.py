'''
problema: beecrowd | 1010
data: 2026.04.16
estudante: Lucas Klipan Miquelin
'''
# objetivo: ler código, quantidade e valor unitário de duas peças e calcular o total a pagar

# --- análise (liac) ---
# entrada: duas linhas; cada uma com código (int), quantidade (int) e valor unitário (float)
# processamento: total = (qtd1 * val1) + (qtd2 * val2)
# Saída: "VALOR A PAGAR: R$ total" com 2 casas decimais

# Lê a primeira lnha e separa os três valores pelo espaço
cod1, qtd1, val1 = input().split()

# Converte quantidade para inteiro e valor unitário para float
qtd1 = int(qtd1)
val1 = float(val1)

# Lê a segunda linha e separa os três valores pelo espaço
cod2, qtd2, val2, = input().split()

# converte quantidade para inteiro e valor unitário para float
qtd2 = int(qtd2)
val2 = float(val2)

# Calcula o valor totál: subtotal da peça 1 + subtotal da peça 2
total = (qtd2 * val2) + (qtd1 * val1)

# exibe o resultado no formato exato exigido pelo enunciado
print(f"VALOR A PAGAR: R$ {total:.02f}")
