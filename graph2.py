import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-13.0, 13.0, 1000)
y = np.linspace(-13.0, 13.0, 1000)
X, Y = np.meshgrid(x,y)
F = np.sin(np.sin(X)+np.cos(Y)) - np.cos(np.sin(X*Y)+np.cos(X))
plt.contour(X,Y,F,[0])

plt.show()
