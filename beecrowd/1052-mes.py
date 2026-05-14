'''
problema: beecrowd | 1052
data: 2026.05.07
estudante: lucas klipan miquelin
'''
#objetivo: classificar um número ao seu mês correspondente em inglês.

# --- ANÁLISE (liac) ---

# entrada: número inteiro
# processamento: ifs e elifs
# saída: mês correspondente ao número, mês na linguagem inglesa.

# entrada:
m = int(input())

# processamento e saída
if m == 1:
    print("January")
elif m == 2:
    print("February")
elif m == 3:
    print("March")
elif m == 4:
    print("April")
elif m == 5:
    print ("May")
elif m == 6:
    print ("June")
elif m == 7:
    print ("July")
elif m == 8:
    print ("August")
elif m == 9:
    print ("September")
elif m == 10:
    print ("October")
elif m == 11:
    print ("November")
elif m == 12:
    print ("December")
    