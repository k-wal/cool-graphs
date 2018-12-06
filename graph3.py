import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-14.0, 16.0, 1000)
y = np.linspace(-12.0, 14.0, 1000)
X, Y = np.meshgrid(x,y)
f1 = np.absolute(np.sin(X)+1)**(np.absolute(np.cos(X))+np.absolute(np.sin(X))+np.exp(np.sin(X)))
f2 = (np.sin(X+Y+X*Y))**2

F = f1-f2
plt.contour(X,Y,F,[0])

plt.show()
