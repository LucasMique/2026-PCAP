/*
Problema 1114 BeeCrowd
2026.09.26
Lucas Klipan Miquelin
*/

#include <stdio.h>

int main() {
    int senha;

    scanf("%d", &senha);

    while (senha != 2002) {
        printf("Senha Invalida\n");
        scanf("%d", &senha);
    
    }

    printf("Acesso Permitido\n");

    return 0;
    
}