import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5.0, 5.0, 1000)
y = np.linspace(-5.0, 5.0, 1000)
X, Y = np.meshgrid(x,y)
F = (1/np.sin(1-X*X))*(1/np.tan(2-Y*Y)) - X*Y
plt.contour(X,Y,F,[0])

plt.show()
