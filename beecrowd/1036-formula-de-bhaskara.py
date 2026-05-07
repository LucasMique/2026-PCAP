'''
problema: beecrowd | 1036
data: 2026.05.07
estudante: Lucas Klipan Miquelin
'''

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

SAHUR =(4 * (A * C)) ** 0.5
if SAHUR ==

TRALALERO = (-B - (((B * B) - (4 * (A * C))) ** 0.5)) / (2 * A)

if TRALALERO == 0 or TRALALERO < 0 or SAHUR == 0 or SAHUR < 0:
    print("Impossivel calcular")
else:
    print(f"R1 = {TRALALERO:.5f}")
    print(f"R2 = {SAHUR:.5f}")

