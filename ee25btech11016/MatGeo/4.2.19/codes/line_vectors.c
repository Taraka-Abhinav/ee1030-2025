#include <stdio.h>

int main() {
    // Equation: x + y = 2
    double n[2] = {1, 1};   // Normal vector
    double m[2] = {1, -1};  // Direction vector

    printf("Normal vector: (%.2f, %.2f)\n", n[0], n[1]);
    printf("Direction vector: (%.2f, %.2f)\n", m[0], m[1]);

    return 0;
}
