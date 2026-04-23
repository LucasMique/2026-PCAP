'''
problema | beecrowd 1012
data: 2026.04.23
estudante: Lucas Klipan Miquelin
'''
# objetivo: escrever um programa para calcular a area de um triângiulo retângulo, um círculo, um trapézio, um quadrado, e um retângulo utilizando variáveis A, B, e C.

# --- Análise (liac) ---
# entrada: 3 valores com float de 1 deimal
# processamento. area de cada uma dessas formas
# saída: nome da forma em maíusculo e valor.

# entradaxxx().split()

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

#pi tbm pq é constante
PI = 3.14159

#processamento aí que terrível proff bersa me salve daqui
TR = (A * C) / 2
CI = (C ** 2) * PI
TRA = (A + B) * (C / 2)
QUA = B ** 2
RET = A * B

#saída. cada um com float de 3
print(f"TRIANGULO: {TR:.3f}")
print(f"CIRCULO: {CI:.3f}")
print(f"TRAPEZIO: {TRA:.3f}")
print(f"QUADRADO: {QUA:.3f}")
print(f"RETANGULO: {RET:.3f}")

