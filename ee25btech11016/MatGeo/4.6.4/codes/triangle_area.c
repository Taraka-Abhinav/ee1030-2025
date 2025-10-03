#include <stdio.h>
#include <math.h>

int main() {
    double a1[3] = {-2, 3, 0};
    double a2[3] = {2, 3, 2};
    double b[3] = {2, -3, 6};
    double da[3], v[3];

    for (int i = 0; i < 3; i++) da[i] = a2[i] - a1[i];

    v[0] = b[1]*da[2] - b[2]*da[1];
    v[1] = b[2]*da[0] - b[0]*da[2];
    v[2] = b[0]*da[1] - b[1]*da[0];

    double vnorm = sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
    double bnorm = sqrt(b[0]*b[0] + b[1]*b[1] + b[2]*b[2]);

    double d = vnorm / bnorm;
    printf("Distance = %lf\n", d);

    return 0;
}
