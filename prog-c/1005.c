/*
Problema 1005 BeeCrowd
2026.09.22
Lucas Klipan Miquelin
*/

#include <stdio.h>

int main(){
    double A=0, B=0, Z=0;
    scanf("%lf", &A);
    scanf("%lf", &B);
    Z = ((A * 3.5) + (B * 7.5)) / 11;
    printf("MEDIA = %.5lf\n", Z);
    return 0;
}