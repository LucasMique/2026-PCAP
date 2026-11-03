/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1049 - Animal
 * Autor     : Lucas Klipan Miquelin
 * LIAC      : Le tres palavras, uma por linha (vertebrado/invertebrado,
 *             a classe e a alimentacao). Imprime o nome do animal.
 */
#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b, c;

    cin >> a >> b >> c;

    if (a == "vertebrado") {
        
        if (b == "ave") {
            if (c == "carnivoro") {
                cout << "aguia" << endl;
            } else {
                cout << "pomba" << endl;
            }
        } else {
            if (c == "onivoro") {
                cout << "homem" << endl;
            } else {
                cout << "vaca" << endl;
            }
        }
    } else {
        if (b == "inseto") {
            if (c == "hematofago") {
                cout << "pulga" << endl;
            } else {
                cout << "lagarta" << endl;
            }
        } else {
            if (c == "hematofago") {
                cout << "sanguessuga" << endl;
            } else {
                cout << "minhoca" << endl;
            }
        }
    }

    return 0;
}