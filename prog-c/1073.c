/*
Problema 1073 BeeCrowd
2026.09.26
Lucas Klipan Miquelin
*/

#include <stdio.h>

int main() {
    int n, i;

    scanf("%d", &n);

    for (i = 2; i <= n; i = i + 2) {
        printf("%d^2 = %d\n", i, i * i);
    }

    return 0;
}   