import numpy as np
import matplotlib.pyplot as plt

# Triangle vertices
A = np.array([0, 5])
B = np.array([3, 2])
C = np.array([-1, 1])
triangle = np.array([A, B, C, A])

# Area calculation
area = 0.5 * abs(np.linalg.det(np.column_stack((A-B, A-C))))
print(f"Area of triangle = {area:.2f}")

# Plot triangle
plt.plot(triangle[:,0], triangle[:,1], 'b-', linewidth=2)
plt.fill(triangle[:,0], triangle[:,1], color='cyan', alpha=0.3)

# Highlight vertices with larger markers
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], 
            color='red', s=100, zorder=5, label='Vertices')

# Annotate vertices
labels = ['A','B','C']
coords = [A,B,C]
for label, coord in zip(labels, coords):
    plt.annotate(label, (coord[0], coord[1]), textcoords="offset points",
                 xytext=(10, 10), ha='center', fontsize=12, color='black', fontweight='bold')

# Plot lines
x_vals = np.linspace(-2, 4, 400)
plt.plot(x_vals, 4*x_vals + 5, 'r--', linewidth=1.5)
plt.plot(x_vals, 5 - x_vals, 'g--', linewidth=1.5)
plt.plot(x_vals, (x_vals + 5)/4, 'm--', linewidth=1.5)

# Annotate line equations near the triangle
plt.text(-1.8, 5.2, '$y=4x+5$', color='r', fontsize=12, fontweight='bold')
plt.text(2.1, 3.5, '$y=5-x$', color='g', fontsize=12, fontweight='bold')
plt.text(0.5, 1.5, '$4y=x+5$', color='m', fontsize=12, fontweight='bold')

# Zoom limits
plt.xlim(-2, 4)
plt.ylim(0, 6)

# Decorations
plt.grid(True)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"Triangle Bounded by Lines, Area = {area:.2f}")
plt.legend()
plt.savefig("triangle_points_lines.png", dpi=200)
plt.show()
