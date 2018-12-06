import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.subplot(211)
x = np.linspace(-5.0, 5.0, 1000)
y = np.linspace(-5.0, 5.0, 1000)
X, Y = np.meshgrid(x,y)
F = np.sin(np.cos(np.tan(X)))*np.sin(np.cos(np.tan(Y)))
plt.contour(X,Y,F,[0])

plt.subplot(212)
x = np.linspace(1.3, 1.7, 1000)
y = np.linspace(1.3, 1.7, 1000)
X, Y = np.meshgrid(x,y)
F = np.sin(np.cos(np.tan(X)))*np.sin(np.cos(np.tan(Y)))
plt.contour(X,Y,F,[0])

plt.show()
