import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C shared library
lib = ctypes.CDLL('./libtriangle.so')
lib.triangle_area.restype = ctypes.c_double
area = lib.triangle_area()
print(f"Area of triangle = {area:.2f}")

# Triangle vertices
A = np.array([0, 5])
B = np.array([3, 2])
C = np.array([-1, 1])
triangle = np.array([A, B, C, A])

# Plot triangle
plt.plot(triangle[:,0], triangle[:,1], 'b-o', label='Triangle')
plt.fill(triangle[:,0], triangle[:,1], color='cyan', alpha=0.3)

# Plot lines
x_vals = np.linspace(-3, 4, 400)
plt.plot(x_vals, 4*x_vals+5, 'r--', label='$y=4x+5$')
plt.plot(x_vals, 5-x_vals, 'g--', label='$y=5-x$')
plt.plot(x_vals, (x_vals+5)/4, 'm--', label='$4y=x+5$')

# Annotate vertices
labels = ['A','B','C']
coords = [A,B,C]
for label, coord in zip(labels, coords):
    plt.annotate(label, (coord[0], coord[1]), textcoords="offset points",
                 xytext=(10, -10), ha='center', fontsize=12, color='black')

# Decorations
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"Triangle Bounded by Lines, Area = {area:.2f}")
plt.savefig("triangle_ctypes_with_lines.png", dpi=200)
plt.show()
