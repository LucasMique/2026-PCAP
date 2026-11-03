/*
* Disciplina: 2026-PCAP
* Problema  : beecrowd 1004 - Produto Simples
* Autor     : Lucas Klipan Miquelin
* LIAC      : Leia dois inteiros e mostre o produto no formato "PROD = produto".
*/
#include <iostream>
using namespace std;

int main () {
    int a, b;

    std::cin >> a >> b;
    std::cout << "PROD = " << a * b << endl;

    return 0;
}