import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load compiled shared library
lib = ctypes.CDLL('./line_distance.so')
lib.main()

# Given data
a1 = np.array([-2, 3, 0])
a2 = np.array([2, 3, 2])
b = np.array([2, -3, 6])

# Compute distance
da = a2 - a1
v = np.cross(b, da)
d = np.linalg.norm(v) / np.linalg.norm(b)
print("Distance =", d)

# Projection of da onto b to find perpendicular foot
proj = (np.dot(da, b) / np.dot(b, b)) * b
perp_vec = da - proj
p1 = a1 + proj
p2 = a2

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Line 1 and Line 2
t = np.linspace(-2, 2, 10)
line1 = a1 + np.outer(t, b)
line2 = a2 + np.outer(t, b)

ax.plot(line1[:,0], line1[:,1], line1[:,2], 'r', label='Line 1')
ax.plot(line2[:,0], line2[:,1], line2[:,2], 'b', label='Line 2')

# Points with vector labels
ax.scatter(*a1, color='red')
ax.text(a1[0], a1[1], a1[2], f"A1 {a1}", color='red', fontsize=10)
ax.scatter(*a2, color='blue')
ax.text(a2[0], a2[1], a2[2], f"A2 {a2}", color='blue', fontsize=10)

# Perpendicular distance line
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'g--', label=f'Distance = {round(d,3)}')

ax.legend()
plt.show()
