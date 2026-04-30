'''
Problema: beecrowd | 1046
data: 2026.04.30
estudante: lucas klipan miquelin
 '''

# input().split() Lê a linha e a quebra em pedaços por espaço
# map(int...) em cada pedaço de uma vez
# os 4 valores são desempacotados nas 4 variantes na ordem
hi, hf = map(int, input().split())

# converte tudo para minutos - fica muito mais fácil calcular duração trabalhando em uma única unidade do que em horas+minutos separados
tim = hi
tfm = hf  

# se o ínicio é maior que o fim, o jogo passou a meia noite (começõu 23h e terminou 2h do dia seguinte) nesse caso somamos 24h (24 * 60m) pra fechar a volta
if tim > tfm:
    ttm = (tfm - tim) + 24
else:
    ttm = tfm - tim

# caso especial: inicio igual a fim = o enunciado diz que o jogo durou 24 h pois a duração mínnima é 1min e a máxima é 24, logo 0 vira 24
if ttm == 0:
    ttm = 24

# converte a duração total de minutos de volta para horas e minutos:
# ttm // 60 - divisão inteira - quantas horas completas cabem
# ttm % 60 - resto - minutos que sobraram
print(f"O JOGO DUROU {ttm} HORA(S)")
