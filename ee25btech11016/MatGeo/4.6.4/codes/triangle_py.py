import numpy as np
import matplotlib.pyplot as plt

# Data
a1 = np.array([-2, 3, 0])
a2 = np.array([2, 3, 2])
b = np.array([2, -3, 6])

# Distance calculation
da = a2 - a1
v = np.cross(b, da)
d = np.linalg.norm(v) / np.linalg.norm(b)
print("Distance =", d)

# Projection for perpendicular line
proj = (np.dot(da, b) / np.dot(b, b)) * b
p1 = a1 + proj
p2 = a2

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Lines
t = np.linspace(-2, 2, 10)
line1 = a1 + np.outer(t, b)
line2 = a2 + np.outer(t, b)

ax.plot(line1[:,0], line1[:,1], line1[:,2], 'r', label='Line 1')
ax.plot(line2[:,0], line2[:,1], line2[:,2], 'b', label='Line 2')

# Points with labels
ax.scatter(*a1, color='red')
ax.text(a1[0], a1[1], a1[2], f"A1 {a1}", color='red', fontsize=10)
ax.scatter(*a2, color='blue')
ax.text(a2[0], a2[1], a2[2], f"A2 {a2}", color='blue', fontsize=10)

# Perpendicular distance line
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'g--', label=f'Distance = {round(d,3)}')

# Direction vectors (as arrows from A1 and A2)
ax.quiver(a1[0], a1[1], a1[2], b[0], b[1], b[2], color='red', arrow_length_ratio=0.1, linewidth=1.5)
ax.text(a1[0]+b[0]*0.5, a1[1]+b[1]*0.5, a1[2]+b[2]*0.5, "b", color='red')

ax.quiver(a2[0], a2[1], a2[2], b[0], b[1], b[2], color='blue', arrow_length_ratio=0.1, linewidth=1.5)
ax.text(a2[0]+b[0]*0.5, a2[1]+b[1]*0.5, a2[2]+b[2]*0.5, "b", color='blue')

# Make plot readable
ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
