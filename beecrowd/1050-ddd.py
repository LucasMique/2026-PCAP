'''
problema: beecrowd | 1050
data: 2026.05.07
estudante: lucas klipan miquelin
'''
# Objetivo: Selecionar DDD de uma lista já predeterminada.

# --- ANÁLISE (liac) ---
# entrada: número de 2 digitos.
#processamento: If e Elifs; caso seja qualquer desses números, dê print do estado com ddd equivalente ao número
#saída: cidades

#entrada: input com int
n = int(input())

# Processamento: ver qual desses é o número; caso um não for, vai para o outro
# saída caso for, dê print na cidade equivalente ao DDD.
if n == 61:
    print("Brasilia")
elif n == 71:
    print("Salvador")
elif n == 11:
    print("Sao Paulo")
elif n == 21:
    print("Rio de Janeiro")
elif n == 32:
    print("Juiz de Fora")
elif n == 19:
    print("Campinas")
elif n == 27:
    print("Vitoria")
elif n == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")