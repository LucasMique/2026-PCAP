# Fliperama do LUCAS

Um fliperama de terminal com três jogos, placar que não 
esquece cadastro de jogadores. Projeto da disciplina PCAP,
primeiro ano do Técnico em Informática do IFPR.

## O que ele faz

- Três jogos pelo menu: Advinhe o Número, Pedra-Papel-Tesoura e Par ou Ímpar
- Placar que conta quantas vezes cada jogo foi jogado e continua contando 
depois de fechar o programa
- Cadastro de jogadores: cadastrar, listar, alterar e excluir.

## Como rodar

```
cd fliperama
python3 main.py
```

## Os arquivos

- `main.py` - o gabinete: menu, placar e chamadas
- `telas.py` - ferramentas visuais
- `modulos.py` - ferramentas de lógica: as três funções que perguntam e conferem
- `placar.py` - quantas partidas cada jogo teve
- `jogadores.py` - quem são os jogadores
- `adivinhe.py`, `ppt.py`, `parimpar.py` - um arquivo por jogo
- `placar.csv` e `jogadores.csv` - os dados, que nascem sozinhos

A função `ler_texto` ficou no `modulos.py` porque é um ferramenta de lógica,
perguntando para a resposta se ela é uma das respostas possíveis e respondendo ela devolta caso sim,
caso não, retorna uma mensagem invalidando o lance.

## De onde ele veio

- Aula 20: os três jogos viraram um programa só, com módulos e menu
- aula 21: entrou o Pedra-Papel-Tesoura e o placar passou a sobreviver
- Aula 22: entrou o cadastro de jogadores, com as quatro operações
- Aula 23: campo em branco barrado e o projeto documentado

## O que ainda não funciona

- Nome com vírcula quebra a linha do arquivo, porque a vírgula é o separador

## Autoavaliacao

Conceito que eu acho que a minha entrega vale: B

### Mapa do projeto: onde esta cada coisa

| O que | Arquivo | Funcao |
|---|---|---|
| Adivinhe o Numero | `adivinhe.py` | `jogar_adivinhe` |
| Pedra-Papel-Tesoura | `ppt.py` | `jogar_ppt` |
| Par ou Impar | `parimpar.py` | `jogar_parimpar` |
| Cara ou Coroa | `meujogo.py` | `jogar_caraoucoroa` |
| Cadastro de jogadores | `jogadores.py` | `menu_jogadores` |
| Ranking Top 10 | `jogadores.py` | `listar` |
| Placar que sobrevive | `placar.py` | `salvar_placar`, `carregar_placar` |

### Criterio por criterio: o nivel e a prova

| Criterio | Nivel | Onde esta a prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura e registro | [B] | [todos os arquivos EXETO .csv e .md, linhas 0-4, 0-6, 0-7, 0-8, ou 0-22, dependendo do arquivo.] |
| 2. As quatro operacoes | [B] | [meujogo.py, linha 36, 47, 50] |
| 3. Busca e indice | [A] | [jogadores.py, 70-85] |
| 4. Persistencia e primeira execucao | [C] | [main.py, 31-61] |
| 5. Documentacao e autoavaliacao | [B] | [meujogo.py, 12, 15, 20, 30, 31, 33, 35, 43, 49, 57, 61.] |
| 6. Jogo autoral e reuso | [A] | [meujogo.py, 22, 24, 25, 44, 45-60. ] |

### Usei IA?

Não.