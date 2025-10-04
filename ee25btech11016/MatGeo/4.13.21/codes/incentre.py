import numpy as np
import matplotlib.pyplot as plt

# Midpoints
D = np.array([0,1])
E = np.array([1,1])
F = np.array([1,0])

# Vertices
A = E + F - D   # (2,0)
B = D + F - E   # (0,0)
C = D + E - F   # (0,2)

# Side lengths
a = np.linalg.norm(C-B)
b = np.linalg.norm(A-C)
c = np.linalg.norm(A-B)

# Incentre
I = (a*A + b*B + c*C) / (a+b+c)

# Plot triangle
plt.figure()
plt.plot([A[0],B[0],C[0],A[0]], [A[1],B[1],C[1],A[1]], 'b-')

# All points with exact coords
points = {
    "A(2,0)": A,
    "B(0,0)": B,
    "C(0,2)": C,
    "D(0,1)": D,
    "E(1,1)": E,
    "F(1,0)": F
}
colors = ['red','green','blue','purple','brown','cyan']

for (label,pt),col in zip(points.items(),colors):
    plt.scatter(pt[0], pt[1], color=col)
    plt.text(pt[0]+0.1, pt[1]+0.1, label)

# Incentre (exact form 2-√2)
plt.scatter(I[0], I[1], color='orange')
plt.text(I[0]+0.1, I[1]+0.1, "I(2-√2,2-√2)", color='orange')

plt.title("Triangle with Midpoints and Incentre")
plt.grid(True)
plt.axis("equal")
plt.show()
