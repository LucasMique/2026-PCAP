'''
problema: beecrowd | 1051
data: 2026.04.30
Estudante: lucas klipan miquelin
'''

dindin = float(input())

if dindin < 2000.00:
    print("Isento")
elif 2000.01 <= dindin < 3000.02:
    dindin = (dindin - 2000) * 0.08
    print(f"R$ {dindin:.2f}")
elif 3000.01 < dindin < 4500.02:
    dindin = ((1000 * 0.08) + ((dindin - 3000) * 0.18))
    print(f"R$ {dindin:.2f}")
elif 4500.01 < dindin:
    dindin = ((1000 * 0.08) + (1500 * 0.18) + ((dindin - 4500) * 0.28))
    print(f"R$ {dindin:.2f}")
