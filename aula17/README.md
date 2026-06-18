# ✊✋✌️ Pedra-Papel-Tesoura
​
Jogo de Pedra-Papel-Tesoura feito em Python na disciplina PCAP (Aula 17).
Você joga contra o computador em uma melhor de 5 rodadas, com placar.
​
## ▶️ Como jogar
1. Abra o terminal na pasta do jogo.
2. Rode: python ppt.py
3. A cada rodada, digite pedra, papel, tesoura, lagarto ou spock.
4. Ao fim das 5 rodadas, o programa mostra o placar final; e você consegue jogar de novo, apenas digitando "sim"
​
## ⚙️ Como funciona (resumo)
A cada rodada o computador sorteia uma jogada (random.choice) com base nas 5 escolhas possíveis e lê a sua.
O texto digitado é limpado, deixando-o todo minúsculo (.lower().strip()) e validado (in) antes de comparar.
Uma sub-rotina decide quem venceu e o programa soma os pontos das 5 rodadas; no fim se digita "sim" ou "não" para terminar o jogo ou jogar-lo de novo.
​
## 🧠 O que eu pratiquei
- Strings e métodos de texto: .lower() e .strip() para limpar o que foi digitado
- Validação com in: aceitar só pedra, papel, tesoura, lagarto, ou spock
- Comparação de textos (==): descobrir empate e vitórias
- random.choice: sortear a jogada da máquina
- Repetição (for): jogar as 5 rodadas e manter o placar
- Condição (while): define se algo acontece enquanto uma váriavel está em certa condição; utilizado para reiniciar o jogo após ganho/perdido
- Sub-rotinas (def/return): isolar a regra do jogo
​
## 🎯 Autoavaliação
Conceito pretendido: A
​
Justificativa (cite arquivo e linha de cada critério):
- O jogo funciona ............: ppt.py, linhas 45 a 68
- Trabalho com texto .........: ppt.py, linhas 14 a 35, 45, 48, 52, 54, 59 a 63, 68.  (.lower().strip(), in, ==, while)
- Documentação e Git .........: este README + commits no GitHub
- Extensão/originalidade .....: ppt.py, linhas  21-34, 41-45, 68 (o que eu criei — Sistema de lagarto e spock aumentando a quantidade de possibilidades de vitórias e percas, e while, fazendo com que o jogo possa ser jogado de novo sem fechar ele.)
​
Autor: Lucas Klipan Miquelin