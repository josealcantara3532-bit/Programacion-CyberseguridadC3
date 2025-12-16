#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <regex>

using namespace std;

struct Equipo {
    string nombre;
    string tipo;
    string ubicacion;
    string ip;
    string estado; // activo / inactivo
};

vector<Equipo> inventario;

bool validarIP(const string& ip) {
    regex patron(
        "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\\.)){3}"
        "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    );
    return regex_match(ip, patron);
}

void registrarEquipo() {
    Equipo eq;

    cout << "\n--- REGISTRO DE EQUIPO ---\n";
    cout << "Nombre del equipo: ";
    getline(cin, eq.nombre);

    cout << "Tipo de equipo: ";
    getline(cin, eq.tipo);

    cout << "Ubicacion: ";
    getline(cin, eq.ubicacion);

    cout << "Direccion IP: ";
    getline(cin, eq.ip);

    if (!validarIP(eq.ip)) {
        cout << "❌ IP invalida.\n";
        return;
    }

    for (auto& e : inventario) {
        if (e.ip == eq.ip) {
            cout << "❌ Ya existe un equipo con esa IP.\n";
            return;
        }
    }

    cout << "Estado (activo/inactivo): ";
    getline(cin, eq.estado);

    if (eq.estado != "activo" && eq.estado != "inactivo") {
        cout << "❌ Estado no valido.\n";
        return;
    }

    inventario.push_back(eq);
    cout << "✅ Equipo registrado correctamente.\n";
}

void mostrarInventario() {
    cout << "\n--- INVENTARIO DE EQUIPOS ---\n";

    if (inventario.empty()) {
        cout << "No hay equipos registrados.\n";
        return;
    }

    cout << left << setw(15) << "Nombre"
         << setw(15) << "Tipo"
         << setw(15) << "Ubicacion"
         << setw(18) << "IP"
         << setw(10) << "Estado" << endl;

    cout << string(73, '-') << endl;

    for (auto& eq : inventario) {
        cout << setw(15) << eq.nombre
             << setw(15) << eq.tipo
             << setw(15) << eq.ubicacion
             << setw(18) << eq.ip
             << setw(10) << eq.estado << endl;
    }
}

void generarAlertas() {
    cout << "\n--- ALERTAS ---\n";
    bool hayAlertas = false;

    for (auto& eq : inventario) {
        if (eq.estado == "inactivo") {
            cout << "⚠️ " << eq.nombre << " (" << eq.ip
                 << ") esta INACTIVO en " << eq.ubicacion << endl;
            hayAlertas = true;
        }
    }

    if (!hayAlertas) {
        cout << "✅ Todos los equipos estan activos.\n";
    }
}

void editarEquipo() {
    string ipBuscar;
    cout << "\nIngrese la IP del equipo a editar: ";
    getline(cin, ipBuscar);

    for (auto& eq : inventario) {
        if (eq.ip == ipBuscar) {
            cout << "Nuevo nombre (enter para mantener): ";
            string temp;
            getline(cin, temp);
            if (!temp.empty()) eq.nombre = temp;

            cout << "Nuevo tipo: ";
            getline(cin, temp);
            if (!temp.empty()) eq.tipo = temp;

            cout << "Nueva ubicacion: ";
            getline(cin, temp);
            if (!temp.empty()) eq.ubicacion = temp;

            cout << "Nuevo estado (activo/inactivo): ";
            getline(cin, temp);
            if (temp == "activo" || temp == "inactivo")
                eq.estado = temp;

            cout << "✅ Equipo actualizado.\n";
            return;
        }
    }

    cout << "❌ Equipo no encontrado.\n";
}

void eliminarEquipo() {
    string ipBuscar;
    cout << "\nIngrese la IP del equipo a eliminar: ";
    getline(cin, ipBuscar);

    for (size_t i = 0; i < inventario.size(); i++) {
        if (inventario[i].ip == ipBuscar) {
            cout << "¿Seguro que desea eliminarlo? (s/n): ";
            char opc;
            cin >> opc;
            cin.ignore();

            if (opc == 's') {
                inventario.erase(inventario.begin() + i);
                cout << "🗑️ Equipo eliminado.\n";
            }
            return;
        }
    }
    cout << "❌ Equipo no encontrado.\n";
}

void mostrarContadores() {
    int activos = 0, inactivos = 0;

    for (auto& eq : inventario) {
        if (eq.estado == "activo") activos++;
        else inactivos++;
    }

    cout << "\nTotal equipos: " << inventario.size() << endl;
    cout << "Activos: " << activos << endl;
    cout << "Inactivos: " << inactivos << endl;
}

void menu() {
    int opcion;

    do {
        cout << "\n===== INVENTARIO DE EQUIPOS DE RED =====\n";
        cout << "1. Registrar equipo\n";
        cout << "2. Mostrar inventario\n";
        cout << "3. Generar alertas\n";
        cout << "4. Editar equipo\n";
        cout << "5. Eliminar equipo\n";
        cout << "6. Mostrar contadores\n";
        cout << "7. Salir\n";
        cout << "Opcion: ";
        cin >> opcion;
        cin.ignore();

        switch (opcion) {
            case 1: registrarEquipo(); break;
            case 2: mostrarInventario(); break;
            case 3: generarAlertas(); break;
            case 4: editarEquipo(); break;
            case 5: eliminarEquipo(); break;
            case 6: mostrarContadores(); break;
            case 7: cout << "Saliendo...\n"; break;
            default: cout << "❌ Opcion invalida.\n";
        }
    } while (opcion != 7);
}

int main() {
    menu();
    return 0;
}
