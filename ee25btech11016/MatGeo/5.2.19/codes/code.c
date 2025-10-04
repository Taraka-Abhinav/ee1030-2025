#include <stdio.h>

typedef struct {
    double x, y;
} Point;

Point solve_linear_system() {
    // Solving manually for the given system
    Point p;
    // x + y = 14
    // x - y = 4
    p.x = (14 + 4)/2; // 9
    p.y = 14 - p.x;   // 5
    return p;
}

int main() {
    Point P = solve_linear_system();
    printf("Intersection Point: P(%g, %g)\n", P.x, P.y);
    return 0;
}
