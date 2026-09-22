/* Comentário de Bloco
Programa: Hello.c
Data: 2026.09.22
Autor: Lucas Klipan Miquelin
*/

// Importa biblioteca padrão de entrada e saída
#include <stdio.h>

// Defino a função principal do tipo int
int main(){
    // printf == Saída --> Mostra na Tela ;
    // "entre aspas == texto"
    // comando se encerra com ;
    // (Mesma coisa que print())
    printf("Hello World!\n");

    // Receber 2 valores, somar e mostrar o resultado
    int A=0, B=0;
    printf("Digite um valor: ");
    scanf("%d", &A);
    printf("Digite outro valor: ");
    scanf("%d", &B);
    int soma = A+B;
    printf("Soma: %d\n", soma);
    // indica que chegou ao fim da função == retornando 0
    return 0 ;
}

/*
para compilar ==
gcc <nome-do-arquivo> -o nome-do-programa
para executar ==
./nome-do-programa
*/