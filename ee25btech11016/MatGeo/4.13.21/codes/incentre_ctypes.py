import ctypes
import matplotlib.pyplot as plt

# Define struct
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

lib = ctypes.CDLL("./incentre.so")
lib.find_incentre.restype = Point
lib.find_incentre.argtypes = [Point, Point, Point]

# Midpoints
D = Point(0,1)
E = Point(1,1)
F = Point(1,0)

# Vertices
A = Point(2,0)
B = Point(0,0)
C = Point(0,2)

# Call C function
I = lib.find_incentre(A,B,C)

# Plot triangle
plt.figure()
plt.plot([A.x,B.x,C.x,A.x], [A.y,B.y,C.y,A.y], 'b-')

points = {
    "A(2,0)": A,
    "B(0,0)": B,
    "C(0,2)": C,
    "D(0,1)": D,
    "E(1,1)": E,
    "F(1,0)": F
}
colors = ['red','green','blue','purple','brown','cyan']

for (label,pt),col in zip(points.items(),colors):
    plt.scatter(pt.x, pt.y, color=col)
    plt.text(pt.x+0.1, pt.y+0.1, label, fontsize=9)

# Incentre exact + numeric
plt.scatter(I.x, I.y, color='orange')
plt.text(I.x+0.1, I.y+0.1, "I(2-√2,2-√2)", color='orange', fontsize=9)

plt.title("Triangle with Midpoints and Incentre (C + Python)")
plt.grid(True)
plt.axis("equal")
plt.show()
