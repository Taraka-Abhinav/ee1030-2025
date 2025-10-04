import numpy as np
import matplotlib.pyplot as plt

# Coefficients for lines
# Line L: x + y = 14
# Line K: x - y = 4

# Define x range for plotting
x_vals = np.linspace(0, 15, 300)

# Line L: y = 14 - x
y_L = 14 - x_vals

# Line K: y = x - 4
y_K = x_vals - 4

# Intersection point (solving manually or using numpy)
A = np.array([[1, 1], [1, -1]])
b = np.array([14, 4])
sol = np.linalg.solve(A, b)
x_int, y_int = sol

# Plot lines
plt.figure()
plt.plot(x_vals, y_L, label='L: x+y=14')
plt.plot(x_vals, y_K, label='K: x-y=4')

# Mark intersection
plt.scatter(x_int, y_int, color='red')
plt.text(x_int+0.3, y_int+0.3, f'P({int(x_int)},{int(y_int)})', color='red')

plt.xlim(0,15)
plt.ylim(0,15)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of Linear System')
plt.grid(True)
plt.legend()
plt.show()
