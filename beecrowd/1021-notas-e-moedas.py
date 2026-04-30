'''
problema: beecrowd | 1021
data: 2026.04.30
estudante: Lucas Klipan Miquelin
'''
# Objetivo: ler um valor monetário e decompô-lo no MENOR número possível
# de notas (100, 50, 20, 10,, 5, 2, 1) e moedas (0.50, 0.25, 0.10, 0.05, 0.01)

# --- ANÁLISE (LIAC) ---
# entrada: um valor monetário com duas casas decimais (ex.: 576.73)
# processamento: separar parte inteira (reais -> notas) e parte decimal (centavos -> moedas)
# usar divisão inteira (//) para descobrir quantas unidades cabem
# e o resto da divisão (%) para guardar o que SOBROU para a proxima troca 
# Saída: lista formatada de nota e moedas, na ordem do maior para o menor valor

# input() lçe o valor como texto (ex.: "576.73"); split(".") corta no ponto
# e devolve uma lista com 2 pedaços: ["576", "73"]
# Atribuição múltipla -> n recebe o primeiro pedaço (reais), m recebe o segundo pedaço (centavos)
n, m = input().split(".")

# converte os pedaços de texto para inteiro, pois faremos contas com eles
n = int(n)    # reais (parte inteira do valor)
m = int(m)    # centavos (parte decimal)

# decomposição dos reais em notas -> sempre da maior para menor>
# // é a divisão inteira (descarta o decimal) -> diz quantas notas daquele valor cabem
# % é o resto da divisão -> guarda o que sobrou para proxima troca

n100 = n // 100; n = n % 100 # quantas notas de 100 cabem; não vira o resto
n50 = n // 50; n = n % 50 # quantas notas de 50 cabem no que sobrou
n20 = n // 20; n = n % 20 # quantas notas de 20 cabem no que sobrou
n10 = n // 10; n = n % 10 # quantas notas de 10 cabem no que sobrou
n05 = n // 5; n = n % 5 # quantas notas de 5 cabem no que sobrou
n02 = n // 2; n = n % 2 # quantas notas de 2 cabem no que sobrou
n01 = n                 # o que sobrou são notas de 1 real

# decomposição dos centavos em moedas: mesma lógica, agora em centavos
# (50,25,10,5 e 1 centavo)
m50 = m // 50; m = m % 50
m25 = m // 25; m = m % 25
m10 = m // 10; m = m % 10
m05 = m // 5; m = m % 5
m01 = m

#saída formatada - exatamente como o juiz online espera (cuidado com a grafia!)
print('NOTAS:')
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n05} nota(s) de R$ 5.00')
print(f'{n02} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{n01} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m05} moeda(s) de R$ 0.05')
print(f'{m01} moeda(s) de R$ 0.01')