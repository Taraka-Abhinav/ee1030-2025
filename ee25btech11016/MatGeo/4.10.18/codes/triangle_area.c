#include <stdio.h>
#include <stdlib.h>

double triangle_area() {
    double Ax = 0, Ay = 5;
    double Bx = 3, By = 2;
    double Cx = -1, Cy = 1;
    double area = 0.5 * ((Ax - Bx)*(Ay - Cy) - (Ax - Cx)*(Ay - By));
    if(area < 0) area = -area;
    return area;
}

int main() {
    double area = triangle_area();
    printf("Area of triangle = %.4f\n", area);
    return 0;
}
