'''
problema: beecrowd
data: 2026.04.09
estudante: Lucas Klipan Miquelin
'''
# Objetivo: Ler nome, saláro fixo e total de vendas; calular e exibir o total a receber

# --- Análise (liac) ---
# Entrada: nome (texto), salário fixo (float), total de vendas efetuadas (float)
# processamento: comissão = vendas * 0.15 -> total = salário fixo + comissão
# saída: exibir no formato exato "TOTAL = R$ valor" com 2 casas decimais

# input() sem conversão -> retorna o nome como texto (str)
n = input()

# float(input()) lê valores monetários (podem ter casas decimais)
s = float(input())
v = float(input())

# O vendedor ganha 15% de comissão sobre o total de vendas
c = v * 0.15

# total a receber = salário fixo + comissão
st = s + c

# :.2f dentro da f-string -> formata o número com exatamente 2 casas decimais
print(f"TOTAL = R$ {st:.2f}")