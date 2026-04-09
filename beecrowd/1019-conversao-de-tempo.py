'''
problema: beecrowd | 1019
data: 2026.04.09
estudante: Lucas Klipan Miquelin
'''
# Objetivo: ler uma duração em segundos e convertê-la para Horas:minutos:segundos

# --- Análise (liac) ---
# Entrada: um numero N inteiro representando segundos totais
# processamento: extrair horas. minutos e segundos restantes por divisão inteira e módulo
# saída: no formato h:m:s (sem zeros á esquerda - 0:9:16, não 00:09:16)

#int(input()) duração sempre é um numero inteiro de segundos
N = int(input())

# // divisão inteira: retorna quantas vezes o divisor cabe no dividendo
# %  módulo: retorna apenas o segundo da divisão

#quantas horas completas cabem em N segundos? (1 hora = 3600 segundos)
h = N // 3600

#segundos restantes após retirar as horas completas
N = N % 3600

# quantos minutos completos cabem nos segundos restantes? (1 min igual 60 segundos)
m = N // 60

# segundos que sobram após retirar os minutos completos
s = N % 60

# f-string monta o formato h:m:s - sem zeros á esquerda

print(f"{h}:{m}:{s}")