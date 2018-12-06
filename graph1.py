import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
x = np.linspace(-2.0, 2.0, 1000)
y = np.linspace(-2.0, 2.0, 1000)
X, Y = np.meshgrid(x,y)
F = (X**2 + Y**2 - 1)**3 - X**2*Y**3
plt.contour(X,Y,F,[0])

plt.show()
