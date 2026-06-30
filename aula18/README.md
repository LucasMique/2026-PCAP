# 🔢 Par ou Ímpar
​
Jogo de Par ou Ímpar feito em Python na disciplina PCAP (Aula 18).
Você joga contra o computador em uma melhor de 5 rodadas, com placar.
​
## ▶️ Como jogar
1. Abra o terminal na pasta do jogo.
2. Rode: python par_impar.py
3. Primeiro, escolha um número de difficuldade para a IA; qualquer número. A cada rodada, escolha a aposta (par ou ímpar) e um número de 0 a 5.
4. Ao fim das 5 rodadas, o programa mostra o placar final. E, caso queira, você pode jogar o jogo de-novo sem fechar o programa.
​
## ⚙️ Como funciona (resumo)
A cada rodada o computador sorteia um número até o número escolhido por você (random.randint) e lê o seu.
A aposta é limpa (.lower().strip()) e validada (in) antes de usar.
A soma dos dois números define a paridade com o operador % (resto).
Uma função decide quem venceu e o programa soma os pontos das 5 rodadas.
​
## 🧠 O que eu pratiquei
- Operador de resto (%): descobrir se a soma é par ou ímpar
- Funções (def/return): isolar a regra do jogo (quem venceu)
- random.randint: sortear o número da máquina
- int(input()): ler o número do jogador, escolher o número de difficuldade para a ia.
- Métodos de texto (.lower().strip()) e validação com in: tratar a aposta
- Repetição (for): jogar as 5 rodadas e manter o placar
​- Repetição (while): re-jogar o jogo sem fechar o programa, utilizando uma variável na base do SIM ou NÃO
## 🎯 Autoavaliação
Conceito pretendido: B
​
Justificativa (cite arquivo e linha de cada critério):
- O jogo funciona ............: par_impar.py, linhas 18, 27-52.
- Funções e operador % .......: par_impar.py, linha 20-24  (def/return, soma % 2)
- Documentação e Git .........: este README + commits no GitHub
- Extensão/originalidade .....: par_impar.py, linha 14-18, 27, 50-52 (o que eu criei — jogar de novo, e escolher a difficuldade)
​
Autor: Lucas Klipan Miquelin