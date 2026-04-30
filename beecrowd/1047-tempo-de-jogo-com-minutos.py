'''
problema: beecrowd | 1047
data: 2026.04.30
estudante: Lucas Klipan Miquelin
'''
# objetivo: calcular a duração de um jogo (em horas e minutos), sabendo a hora de inicio (hi:mi) e a hora de fim (hf:mf), o jogo dura no mínimo 1 minuto e no máximo 24 horas.

# análise liac
# entrada: 4 inteiros na mesma linha (hi mi hf mh (hora/minuto inicial e final))
# processamento: converter início e fim para o total e minutos: se o fim for menor o igual ao início, o jogo virou a noite (somar 24h em minutos); converter a duração de volta para horas e mintos
# saída " o jogo durou h horas e m minutos"

# input().split() Lê a linha e a quebra em pedaços por espaço
# map(int...) em cada pedaço de uma vez
# os 4 valores são desempacotados nas 4 variantes na ordem
hi, mi, hf, mf, = map(int, input().split())

# converte tudo para minutos - fica muito mais fácil calcular duração trabalhando em uma única unidade do que em horas+minutos separados
tim = (hi * 60) + mi # tempo inicial em m´nutos
tfm = (hf * 60) + mf # tempo final em minutos

# se o ínicio é maior que o fim, o jogo passou a meia noite (começõu 23h e terminou 2h do dia seguinte) nesse caso somamos 24h (24 * 60m) pra fechar a volta
if tim > tfm:
    ttm = (tfm - tim) + (24 * 60)
else:
    ttm = tfm - tim

# caso especial: inicio igual a fim = o enunciado diz que o jogo durou 24 h pois a duração mínnima é 1min e a máxima é 24, logo 0 vira 24
if ttm == 0:
    ttm = 24 * 60

# converte a duração total de minutos de volta para horas e minutos:
# ttm // 60 - divisão inteira - quantas horas completas cabem
# ttm % 60 - resto - minutos que sobraram
print(f"O JOGO DUROU {ttm // 60} HORA(S) E {ttm % 60} MINUTO(S)")
