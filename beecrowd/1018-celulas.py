'''
problema: beecrowd | 1018
data: 2026.04.30
estudante: Lucas Klipan Miquelin
'''
# não vai ter nada pois haja problema longo mds
n = int(input())

#processamento grah
m = n
n100 = m // 100; m = m % 100
n50 = m // 50; m = m % 50
n20 = m // 20; m = m % 20
n10 = m // 10; m = m % 10
n05 = m // 5; m = m % 5
n02 = m // 2; m = m % 2
n01 = m

#saída
print(f'{n}')
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n05} nota(s) de R$ 5,00')
print(f'{n02} nota(s) de R$ 2,00')
print(f'{n01} nota(s) de R$ 1,00')