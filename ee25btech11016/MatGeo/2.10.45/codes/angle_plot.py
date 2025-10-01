import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load C shared library
lib = ctypes.CDLL("./angle_vectors.so")

# Define argtypes and restype
lib.find_angle.argtypes = [ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double)]
lib.find_angle.restype = ctypes.c_double

# Define vectors
a = (ctypes.c_double * 2)(1, 0)
b = (ctypes.c_double * 2)(0.5, np.sqrt(3)/2)

# Call C function
theta = lib.find_angle(a, b) * 180 / np.pi
print("Angle between vectors =", theta, "degrees")

# Plot vectors
origin = np.array([0,0])
A = np.array([1,0])
B = np.array([0.5,np.sqrt(3)/2])

plt.quiver(*origin, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(*origin, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='b')

# Label points
plt.text(A[0]+0.05, A[1], 'A', fontsize=12, color='r')
plt.text(B[0]+0.05, B[1], 'B', fontsize=12, color='b')
plt.text(0, 0, 'O', fontsize=12, color='k')

# Display angle near origin
plt.text(0.2, 0.1, f"{theta:.2f}°", fontsize=12, color='purple')

plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)
plt.grid(True)
plt.gca().set_aspect('equal')
plt.title("Vectors with angle between them")
plt.show()
