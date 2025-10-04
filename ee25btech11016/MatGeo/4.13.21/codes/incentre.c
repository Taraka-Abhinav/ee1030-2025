#include <stdio.h>
#include <math.h>

typedef struct {
    double x, y;
} Point;

Point make_point(double x, double y) {
    Point p; p.x = x; p.y = y; return p;
}

double dist(Point p1, Point p2) {
    return sqrt(pow(p1.x - p2.x,2) + pow(p1.y - p2.y,2));
}

Point find_incentre(Point A, Point B, Point C) {
    double a = dist(B,C);
    double b = dist(A,C);
    double c = dist(A,B);

    Point I;
    I.x = (a*A.x + b*B.x + c*C.x) / (a+b+c);
    I.y = (a*A.y + b*B.y + c*C.y) / (a+b+c);
    return I;
}

int main() {
    Point D = make_point(0,1);
    Point E = make_point(1,1);
    Point F = make_point(1,0);

    Point A = make_point(2,0);
    Point B = make_point(0,0);
    Point C = make_point(0,2);

    Point I = find_incentre(A,B,C);

    printf("Vertices:\nA(2,0)\nB(0,0)\nC(0,2)\n");
    printf("Midpoints:\nD(0,1)\nE(1,1)\nF(1,0)\n");
    printf("Incentre: I(2-√2, 2-√2)\n");
    printf("Numeric Incentre: (%.4f, %.4f)\n", I.x, I.y);

    return 0;
}
