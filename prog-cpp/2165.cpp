/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 2165 - Twitting
 * Autor     : Lucas Klipan Miquelin
 * LIAC      : Le uma linha de texto (pode ter espacos). Se tiver ate 140
 *             caracteres imprime "TWEET"; se tiver mais, "MUTE".
 */
#include <iostream>
#include <string>
using namespace std;

int main() {
    string texto;

    getline(cin, texto);
    if (texto.size() <= 140) {
        cout << "TWEET" << endl;
    } else {
        cout << "MUTE" << endl;
    }

    return 0;
}