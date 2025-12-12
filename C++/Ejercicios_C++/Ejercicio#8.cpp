#include <iostream>
using namespace std;

int main() {
    int num, suma = 0;

    cout << "Ingrese numeros (0 para terminar):\n";
    cin >> num;

    while (num != 0) {
        suma += num;
        cin >> num;
    }

    cout << "Suma total: " << suma << endl;
    return 0;
}

