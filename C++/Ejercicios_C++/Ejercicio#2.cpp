#include <iostream>
using namespace std;

int main() {
    string nombre;
    int edad;
    float estatura;

    cout << "Nombre: ";
    getline(cin, nombre);

    cout << "Edad: ";
    cin >> edad;

    cout << "Estatura: ";
    cin >> estatura;

    cout << "\n---- FICHA ----\n";
    cout << "Nombre: " << nombre << endl;
    cout << "Edad: " << edad << endl;
    cout << "Estatura: " << estatura << " m" << endl;

    return 0;
}

