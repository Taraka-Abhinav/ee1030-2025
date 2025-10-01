import numpy as np
import matplotlib.pyplot as plt

# Define unit vectors
A = np.array([1, 0])                  # endpoint of vector a
B = np.array([0.5, np.sqrt(3)/2])     # endpoint of vector b
O = np.array([0, 0])                  # origin

# Compute angle
dot = np.dot(A, B)
theta = np.degrees(np.arccos(dot / (np.linalg.norm(A) * np.linalg.norm(B))))
print("Angle between vectors =", theta, "degrees")

# Plot vectors
plt.quiver(*O, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(*O, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='b')

# Label endpoints
plt.text(A[0]+0.05, A[1], 'A', fontsize=12, color='r')
plt.text(B[0]+0.05, B[1], 'B', fontsize=12, color='b')
plt.text(0, 0, 'O', fontsize=12, color='k')

# Display angle
plt.text(0.2, 0.1, f"{theta:.2f}°", fontsize=12, color='purple')

plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)
plt.grid(True)
plt.gca().set_aspect('equal')
plt.title("Vectors OA and OB with angle between them")
plt.show()
