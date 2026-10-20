/*
* Disciplina: 2026-PCAP
* Projeto   : MeuApp v3.0 - o Fliperama em C (Aula 28)
* Autor     : Lucas Klipan Miquelin
* LIAC      : Menu com valiacao, cadastro de jogadores em vetores com
*             contagem, um jogo que conta partidas por jogador e o
*             cadastro salvo em arquivo na saida e relido na entrada.
*/
#include <stdio.h>
#include <string.h>

#define DONO "LUCAS"
#define CAPACIDADE 50
#define TAM_APELIDO 20

void linha() {
    printf("======================================\n");
}

void titulo(char texto[]) {
    linha();
    printf("    %s\n", texto);
    linha();
}

int ler_numero(char mensagem[], int minimo, int maximo) {
    int numero, lidos;

    printf("%s: ", mensagem);
    lidos = scanf("%d", &numero);
    while (lidos != 1 || numero < minimo || numero > maximo) {
        if (lidos != 1) {
            scanf("%*s");     /* joga fora o que nao era numero*/
        }
        printf("Opcao invalida! Tente de novo: ");
        lidos = scanf("%d", &numero);
    }
    return numero;
}

void ler_texto(char mensagem[], char destino[]) {
    printf("%s: ", mensagem);
    scanf("%19s", destino);  /* uma palavra, no maximo 19 letras*/
}

int buscar(char apelidos[][TAM_APELIDO], int qtd, char procurado[]) {
    int i;

    for (i = 0; i < qtd; i++) {
        if (strcmp(apelidos[i], procurado) == 0) {
            return i;
        }
    }
    return -1;
}

int cadastrar(char apelidos[][TAM_APELIDO], int partidas[], int qtd) {
    char novo[TAM_APELIDO];

    titulo("NOVO JOGADOR");
    ler_texto("Apelido (sem espacos)", novo);

    if (buscar(apelidos, qtd, novo) != -1) {
        printf("Ese apelido ja esta cadastrado.\n");
        return qtd;
    }

    strcpy(apelidos[qtd], novo);
    partidas[qtd] = 0;
    printf("Jogador %s cadastrado.\n", novo);
    return qtd + 1;
}

void listar(char apelidos[][TAM_APELIDO], int partidas[], int qtd) {
    int i;

    titulo("JOGADORES CADASTRADOS");
    if (qtd == 0) {
        printf("Nenhum jogador cadastrado ainda.\n");
    }
    for (i = 0; i < qtd; i++) {
        printf("%s | %d partidas \n", apelidos[i], partidas[i]);
    }
}

void mostrar_menu() {
    linha();
    printf("    FLIPERAMA DO %s\n", DONO);
    linha();
    printf("[1] Advinhe o Numero\n");
    printf("[2] Cadastrar jogador\n");
    printf("[3] Listar jogadores\n");
    printf("[0] Sair\n");
    linha();
}

int main() {
    char apelidos[CAPACIDADE][TAM_APELIDO];
    int partidas[CAPACIDADE];   
    int qtd, opcao;

    qtd = 0;

    mostrar_menu();
    opcao = ler_numero("Sua escolha", 0, 3);
    while (opcao !=0) {
        if (opcao == 1) {
            printf("O jogo entra na Fase 3.\n");
        } else if (opcao == 2) {
            qtd = cadastrar(apelidos, partidas, qtd);
        } else {
            listar(apelidos, partidas, qtd);
        }
        mostrar_menu();
        opcao = ler_numero("Sua escolha", 0, 3);
    }

    titulo("Ate a proxima!");
    return 0;
}