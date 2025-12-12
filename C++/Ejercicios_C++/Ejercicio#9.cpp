#include <iostream>
using namespace std;

int main() {
    int opcion, a, b;

    do {
        cout << "\n--- MENU ---\n";
        cout << "1. Sumar\n";
        cout << "2. Restar\n";
        cout << "3. Multiplicar\n";
        cout << "4. Salir\n";
        cout << "Opcion: ";
        cin >> opcion;

        if (opcion >= 1 && opcion <= 3) {
            cout << "Ingrese el primer numero: ";
            cin >> a;

            cout << "Ingrese el segundo numero: ";
            cin >> b;
        }

        switch(opcion) {
            case 1:
                cout << "Resultado: " << a + b << endl;
                break;
            case 2:
                cout << "Resultado: " << a - b << endl;
                break;
            case 3:
                cout << "Resultado: " << a * b << endl;
                break;
            case 4:
                cout << "Saliendo..." << endl;
                break;
            default:
                cout << "Opcion invalida" << endl;
        }

    } while(opcion != 4);

    return 0;
}

