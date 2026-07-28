# 1. váriáveis
idade = 15
ano = 2026
# 2. operadores
20 + 380 == 20 ** 2
# 3. entrada de dados
nome = input("Qual seu nome? ")
# 4. saída de dados
print(f"Olá {nome}!")
# 5. estrutura de repetição
for idade in range(1, idade):
    print("Olá senhor berssa.")
# 6. Estrutura de condição
if ano - idade >= 2010:
    print("Oloko você nasceu depois de 2010!")
# 7. sub-rotinas
def resenha(nota, sete):
    if nota >= sete:
        return True
    if nota <= sete:
        return False

sete = 7
nota = int(input("Insira sua nota:(Nota passável é 7=>) "))
retorno = resenha(nota, sete)
if retorno == False:
    print("Não passou.")
elif retorno == True:
    print("Passou.")