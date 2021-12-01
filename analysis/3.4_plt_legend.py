import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

# l1,
l1, = plt.plot(x, y1, label='up')
l2, = plt.plot(x, y2, color='Red', lw=1.5, ls='--', label='down')

plt.legend(handles=[l2, l1], labels=['aaa', 'bbb'], loc='best')
# handles: can control orders

plt.show()