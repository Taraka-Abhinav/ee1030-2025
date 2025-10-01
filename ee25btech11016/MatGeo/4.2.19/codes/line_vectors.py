import numpy as np
import matplotlib.pyplot as plt

# Given line: y = -x + 2
n = np.array([1, 1])   # Normal vector
m = np.array([1, -1])  # Direction vector

print("Normal vector =", n)
print("Direction vector =", m)

# Plot the line
x_vals = np.linspace(-2, 4, 100)
y_vals = -x_vals + 2

plt.plot(x_vals, y_vals, 'g', label="Line y = -x + 2")

# Show vectors at point (1,1) on the line
point = np.array([1, 1])
plt.quiver(point[0], point[1], n[0], n[1], angles="xy", scale_units="xy", scale=1, color='r', label="Normal Vector n")
plt.quiver(point[0], point[1], m[0], m[1], angles="xy", scale_units="xy", scale=1, color='b', label="Direction Vector m")

plt.text(point[0]+0.2, point[1]+0.2, "Point (1,1)", fontsize=10)
plt.grid(True)
plt.gca().set_aspect('equal')
plt.legend()
plt.title("Line with Normal & Direction Vectors")
plt.show()
