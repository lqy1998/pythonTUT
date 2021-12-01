import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure(num=5, figsize=(8,5))
plt.plot(x, y1)
plt.plot(x, y2, color='DarkRed', lw=10, ls='--')
# lw = linewidth   ls = linestyle

plt.show()