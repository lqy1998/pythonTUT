import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure(num=1, figsize=(8,5))
plt.plot(x, y1)
plt.plot(x, y2, color='Red', lw=1.5, ls='--')

plt.xlim(-1, 2)
plt.ylim(-2, 3)

plt.xlabel("I an x")
plt.ylabel("I an y")

new_ticks = np.linspace(-1, 2, 10)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', '$bad\ \\alpha$', 'normal', 'good', r'$very good$'])

# gca = get current axis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 1.22))
ax.spines['left'].set_position(('data', 0))
# outward, axes

plt.show()