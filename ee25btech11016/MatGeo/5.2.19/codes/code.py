import ctypes
import numpy as np
import matplotlib.pyplot as plt

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

lib = ctypes.CDLL("./solve_linear.so")
lib.solve_linear_system.restype = Point

P = lib.solve_linear_system()

# Plotting
x_vals = np.linspace(0, 15, 300)
y_L = 14 - x_vals
y_K = x_vals - 4

plt.figure()
plt.plot(x_vals, y_L, label='L: x+y=14')
plt.plot(x_vals, y_K, label='K: x-y=4')

plt.scatter(P.x, P.y, color='red')
plt.text(P.x+0.3, P.y+0.3, f'P({int(P.x)},{int(P.y)})', color='red')

plt.xlim(0,15)
plt.ylim(0,15)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of Linear System (C + Python)')
plt.grid(True)
plt.legend()
plt.show()
