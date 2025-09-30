import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load compiled C library
lib = ctypes.CDLL("./triangle_area.so")

# Define argument and return types
lib.area_triangle.argtypes = [ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]
lib.area_triangle.restype = ctypes.c_double

# Define points
A = (ctypes.c_double * 3)(2,3,0)
B = (ctypes.c_double * 3)(3,5,0)
C = (ctypes.c_double * 3)(4,4,0)

# Call C function
area = lib.area_triangle(A,B,C)
print("Area of triangle =", area)

# Plot triangle
points = np.array([[2,3],[3,5],[4,4],[2,3]])
plt.plot(points[:,0], points[:,1], 'bo-')
for i, txt in enumerate(['A','B','C']):
    plt.text(points[i,0]+0.1, points[i,1]+0.1, txt, fontsize=12)
plt.title(f"Triangle ABC (Area = {area:.2f})")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()
