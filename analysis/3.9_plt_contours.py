import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# use plt.contourf to filling contours    8:groups num
X,Y = np.meshgrid(x, y)
plt.contourf(X, Y, f(X, Y), 80, alpha=.75, cmap=plt.cm.hot)

# contour lines   
C = plt.contour(X, Y, f(X, Y), 80, colors='black', linewidths=0.05)

# adding label
plt.clabel(C, inline=True, fontsize=5)

plt.xticks()
plt.yticks()
plt.show()