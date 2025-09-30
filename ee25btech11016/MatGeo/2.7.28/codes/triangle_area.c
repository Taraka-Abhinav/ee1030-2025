#include <stdio.h>
#include <math.h>

// Function to compute cross product magnitude in 3D
double area_triangle(double A[3], double B[3], double C[3]) {
    double AB[3] = {A[0] - B[0], A[1] - B[1], 0};
    double AC[3] = {A[0] - C[0], A[1] - C[1], 0};
    double cross[3] = {
        AB[1]*AC[2] - AB[2]*AC[1],
        AB[2]*AC[0] - AB[0]*AC[2],
        AB[0]*AC[1] - AB[1]*AC[0]
    };
    double mag = sqrt(cross[0]*cross[0] + cross[1]*cross[1] + cross[2]*cross[2]);
    return 0.5 * mag;
}

int main() {
    double A[3] = {2,3,0};
    double B[3] = {3,5,0};
    double C[3] = {4,4,0};

    double area = area_triangle(A,B,C);
    printf("Area of triangle = %.2f\n", area);

    FILE *fp = fopen("triangle_points.txt","w");
    fprintf(fp,"%f %f\n", A[0], A[1]);
    fprintf(fp,"%f %f\n", B[0], B[1]);
    fprintf(fp,"%f %f\n", C[0], C[1]);
    fprintf(fp,"%f %f\n", A[0], A[1]); // close loop
    fclose(fp);

    return 0;
}
