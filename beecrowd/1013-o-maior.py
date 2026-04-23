'''
problema | beecrowd 1013
data: 2026.04.23
estudante: Lucas Klipan Miquelin
'''
# objetivo: ver qual número entre 3 valores é o maior

# --- análise (liac) ---
# entrada: 3 valores
# processamento: (a+b+abs(a-b)
# Saída: "xxx eh o maior"

# entrada... mds

A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

# processamento... Deus me tenha
MAIORAB = (A + B + abs(A - B)) // 2

if MAIORAB is A:
    MAIORAB = (A + C + abs(A - C)) // 2
elif MAIORAB is B:
    MAIORAB = (B + C + abs(B - C)) // 2

# saída?

print(f"{MAIORAB:.0f} eh o maior")