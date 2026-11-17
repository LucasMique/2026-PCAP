# Fliperama em C++ (MeuApp v4.0)

## O que e
Programa de fliperama que cadastra jogadores e os lista. Roda o jogo "Adivinhe o Numero" (de 1 a 100) e conta quantas partidas cada jogador terminou.
Programa derivado dos diversos outros fliperamas que eu já fiz.

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: o programa inteiro (menu, cadastro, jogo, salvar e carregar)
- jogadores.csv: uma linha por jogador, no formato apelido,partidas (nome e numero de partidas terminadas)

## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
| guardar um jogador | strcpy(apelidos[qtd], novo) (l. 77) | apelidos.push_back(novo) (l. 98) |
| comparar apelidos | strcmp(apelidos[i], procurado) == 0 (l. 53) | apelidos[i] == procurado (l. 58) |
| a funcao que cadastra | int cadastrar(..., int qtd) (l. 60) | void cadastrar(... &apelidos, ...) (l. 87) |
| gravar em arquivo | fopen(ARQUIVO, "w") (l. 128) | ofstream arquivo(ARQUIVO) (l. 66) |
| cadastro cheio | if (qtd >= CAPACIDADE) (l. 65) | nao existe: o vector cresce sozinho |
| quantos jogadores existem | int qtd passado de funcao em funcao (l. 165) | apelidos.size() (l. 55) |

## O que o C++ decidiu por mim
Em C, cadastrar devolvia qtd + 1 (l. 80) para a main saber quantos jogadores existiam, e eu cuidava do limite de 50 na mao.
Em C++ cadastrar e void, porque o proprio vector guarda o tamanho (size()) e cresce sozinho a cada push_back.

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | B | fliperama.cpp l. 1-15 (cabecalho e includes), l. 178 (main); .gitignore; commits: [seu historico, um por fase] |
| 2. Cadastro: vectors e referencia | B | fliperama.cpp l. 87-102 (cadastrar, recusa de repetido nas l. 93-96), l. 54 (buscar), l. 116-132 (excluir, erase nos dois vectors nas l. 128-129) |
| 3. Jogo e partidas | B | fliperama.cpp l. 134-165 (jogar_advinhe), l. 161 (tentativas mostradas), l. 163-164 (partidas[pos] + 1 e salvar ao terminar) |
| 4. Persistencia | B | fliperama.cpp l. 65 (salvar), l. 74 (carregar), l. 100 (salvar apos cadastrar), l. 130 (salvar apos excluir), l. 184 e 202 (carregar e salvar na main), jogadores.csv |
| 5. Documentacao e comparacao | B | README.md (tabela C x C++ com seis linhas e secao "O que o C++ decidiu por mim") |