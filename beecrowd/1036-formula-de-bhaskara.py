'''
problema: beecrowd | 1036
data: 2026.05.07
estudante: Lucas Klipan Miquelin
'''

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

TUNG =((B ** 2) - (4 * (A * C)))
if TUNG <= 0:
    print("Impossivel calcular")
else:
    TUNG = TUNG ** 0.5
    SAHUR = (-B + TUNG) / (A * 2)
    TRALALERO = (-B - TUNG) / (A * 2)
    print(f"R1 = {SAHUR:.5f}")
    print(f"R2 = {TRALALERO:.5f}")

# Quem construiu a máquina que constrói maquinas?
# Essa frase é falsa.
# Um conjunto de conjuntos contém a si mesmo?
# Nova missão: Não faça essa missão.