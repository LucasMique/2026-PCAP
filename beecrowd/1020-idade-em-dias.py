'''
problema: beecrowd | 1020
data: 2026.04.09
estudante: Lucas Klipan Miquelin
'''
# Objetivo: ler dias e converter em ano, meses, e dias

# --- Análise (liac) ---
# Entrada: um número D inteiro lendo dias
# processamento: pegar dias, meses
# saída: no formato h:m:s (sem zeros á esquerda - 0:9:16, não 00:09:16)

#int(input()) duração sempre é um numero inteiro de dias
N = int(input())

# // divisão inteira: retorna quantas vezes o divisor cabe no dividendo
# %  módulo: retorna apenas o segundo da divisão

#quantos anos completos cabem em N dias? (1 ano = 365 dias)
h = N // 365

#dias restantes após retirar os anos completos
N = N % 365

# quantos meses completos cabem nos dias restantes? (1 mes igual 30 dias)
m = N // 30

# dias que sobram após retirar os meses completos
s = N % 30

# f-string monta o formato h:m:s - sem zeros á esquerda

print(f"{h} ano(s)")
print(f"{m} mes(es)")      
print(f"{s} dia(s)")