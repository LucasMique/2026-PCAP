# Cara ou Coroa

Jogo autoral do meu fliperama. Abre pela opcao [4] do menu.
Autor: Lucas Klipan Miquelin
## A regra

Utiliando 0 ou 1, o jogador escolhe Cara ou Coroa, respectivamente.
O Computador sortea um número, de 1 a 1000, e caso o número seja par, é cara, e caso é ímpar, a moeda cái como coroa.
Caso a escolha do jogador for uma previsão da jogada correta, ele ganha um ponto.
O jogo acaba quando ou o jogador atinge 2 pontos ou o computador atinge 2 pontos.

## Como jogar

1. Dentro da pasta `fliperama`, rode `python3 main.py`.
2. Escolha a opcao `[4]` no menu.
3. Digite 0 ou 1, dependendo se quer jogar cara ou coroa.

## O que eu reusei do projeto, e onde

| Peca | De qual modulo | Onde eu uso | Para que serve ali |
|---|---|---|---|
| `titulo()` | `telas.py` | `meujogo.py`, linha [20] | desenha a testeira do jogo |
| `linha()` | `telas.py` | `meujogo.py`, linha [41, 50] | fecha a tela no fim da partida |
| `ler_opcao()` | `modulos.py` | `meujogo.py`, linha [28] | pede a entrada e recusa fora das escolhas pre-determinadas. |

## Exemplo de execucao

```
****************************************
             CARA OU COROA              
****************************************
[0] Cara
[1] Coroa
Sua jogada:  1
VOCÊ SELECIONOU COROA
A MOEDA CAIU, E SEU RESULTADO FOI CARA
****************************************
Você errou!
****************************************
Placar: Jogador 0 X 1 computador 
[0] Cara
[1] Coroa
Sua jogada:  1
VOCÊ SELECIONOU COROA
A MOEDA CAIU, E SEU RESULTADO FOI COROA
****************************************
Você acertou!
****************************************
Placar: Jogador 1 X 1 computador 
[0] Cara
[1] Coroa
Sua jogada:  1
VOCÊ SELECIONOU COROA
A MOEDA CAIU, E SEU RESULTADO FOI COROA
****************************************
Você acertou!
****************************************
Placar: Jogador 2 X 1 computador 
****************************************
              VOCÊ VENCEU!              
```

## O que ainda nao funciona

- Nada