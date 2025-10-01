import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./line_vectors.so")

# Define C function signature
lib.get_vectors.argtypes = [ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double)]

def get_vectors():
    n = (ctypes.c_double * 2)()
    m = (ctypes.c_double * 2)()
    lib.get_vectors(n, m)
    return np.array([n[0], n[1]]), np.array([m[0], m[1]])

# Call C function
n, m = get_vectors()
print("Normal vector:", n)
print("Direction vector:", m)

# Plot the line y = -x + 2
x_vals = np.linspace(-2, 4, 100)
y_vals = -x_vals + 2

# Plot line
plt.plot(x_vals, y_vals, 'g', label="Line y = -x + 2")

# Show normal vector at a point on the line (e.g., (1,1))
point = np.array([1, 1])
plt.quiver(point[0], point[1], n[0], n[1], angles="xy", scale_units="xy", scale=1, color='r', label="Normal Vector n")
plt.quiver(point[0], point[1], m[0], m[1], angles="xy", scale_units="xy", scale=1, color='b', label="Direction Vector m")

plt.text(point[0]+0.2, point[1]+0.2, "Point on Line", fontsize=10)
plt.grid(True)
plt.gca().set_aspect('equal')
plt.legend()
plt.title("Line with Normal & Direction Vectors")
plt.show()
