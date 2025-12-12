#include <iostream>
using namespace std;

int main() {
    float c, f;
    cout << "Ingrese grados Celsius: ";
    cin >> c;

    f = (c * 9/5) + 32;

    cout << "Fahrenheit: " << f << endl;
    return 0;
}

