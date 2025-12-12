#include <iostream>
using namespace std;

struct Estudiante {
    string nombre;
    int edad;
    float promedio;
};

int main() {
    Estudiante est[3];
    float mejor = -1;
    string mejorNombre;

    for (int i = 0; i < 3; i++) {
        cout << "\nEstudiante " << i+1 << endl;
        cout << "Nombre: ";
        cin >> est[i].nombre;
        cout << "Edad: ";
        cin >> est[i].edad;
        cout << "Promedio: ";
        cin >> est[i].promedio;

        if (est[i].promedio > mejor) {
            mejor = est[i].promedio;
            mejorNombre = est[i].nombre;
        }
    }

    cout << "\nEl mejor promedio es de " << mejorNombre << " con " << mejor << endl;
    return 0;
}

