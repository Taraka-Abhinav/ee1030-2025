import numpy as np
import matplotlib.pyplot as plt

# Define points
A = np.array([2,3,0])
B = np.array([3,5,0])
C = np.array([4,4,0])

# Vectors
AB = A - B
AC = A - C

# Cross product & area
cross = np.cross(AB,AC)
area = 0.5 * np.linalg.norm(cross)
print("Area of triangle =", area)

# Plot triangle
points = np.array([[2,3],[3,5],[4,4],[2,3]])
plt.plot(points[:,0], points[:,1], 'ro-')
for i, txt in enumerate(['A','B','C']):
    plt.text(points[i,0]+0.1, points[i,1]+0.1, txt, fontsize=12)
plt.title(f"Triangle ABC (Area = {area:.2f})")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()
