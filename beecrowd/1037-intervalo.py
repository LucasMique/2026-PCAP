'''
problema: beecrowd | 1037
data: 2026.04.16
estudante: Lucas Klipan Miquelin
'''
# Objetivo: ler um valor float e indicar em qual intervalo ele se encontra

# --- análise (liac) ---
# entrada: um número de ponto flutuante qualquer
# Processamento: verificar em qual dos intervalos o valor se enquadra
# saída: mensagem com o intervalo correspondente ou "Fora de intervalo"

valor = float(input())

# cada elif só é testado se todas as condições anteriores foram falsas
# Isso elimina a nessecidade de ifs alinhados - código mais limpo e legível
if 0 <= valor <= 25:
    # colchete | indica que o extremo está incluído no intervalo
    print("Intervalo [0,25]")
elif 25 < valor <= 50:
    # Parêntese: ( indica que 25 não está incluido - apenas valores maiores que 25
    print("Intervalo (25,50]")
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
elif 75 < valor <= 100:
    print("Intervalo (75, 100]")
else:
    # Nenhum intervalo correspondeu: Valor negativo ou acima de 100
    print("Fora de intervalo")