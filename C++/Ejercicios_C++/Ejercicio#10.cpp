#include <iostream>
using namespace std;

int main() {
    int num, pares = 0, impares = 0;

    cout << "Ingrese 10 numeros:\n";
    for (int i = 0; i < 10; i++) {
        cin >> num;
        if (num % 2 == 0)
            pares++;
        else
            impares++;
    }

    cout << "Pares: " << pares << endl;
    cout << "Impares: " << impares << endl;

    return 0;
}
