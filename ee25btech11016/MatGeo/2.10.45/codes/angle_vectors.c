#include <stdio.h>
#include <math.h>

// Function to compute angle between two vectors
double find_angle(double a[2], double b[2]) {
    double dot = a[0]*b[0] + a[1]*b[1];
    double mag_a = sqrt(a[0]*a[0] + a[1]*a[1]);
    double mag_b = sqrt(b[0]*b[0] + b[1]*b[1]);
    return acos(dot / (mag_a * mag_b));
}

int main() {
    // Unit vectors with 60° between them
    double a[2] = {1, 0};
    double b[2] = {0.5, sqrt(3)/2};

    double theta = find_angle(a,b);
    printf("Angle between vectors = %.2f degrees\n", theta*180/M_PI);

    // Save points for plotting
    FILE *fp = fopen("vectors.txt", "w");
    fprintf(fp, "0 0 %f %f\n", a[0], a[1]);
    fprintf(fp, "0 0 %f %f\n", b[0], b[1]);
    fclose(fp);

    return 0;
}
