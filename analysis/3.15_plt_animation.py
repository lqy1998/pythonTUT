import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/50.0))  # update the data, control peed
    return line

# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.sin(x))
    return line,

# call the animator
# interval= update frequency
# blit=True   only re-draw the parts that have changed
# blit=False  all update

ani = animation.FuncAnimation(fig=fig, func=animate, 
                              frames=100, init_func=init,
                              interval=20, blit=False)
plt.show()

# save the animation as an mp4.  
# This requires ffmpeg or mencoder to be installed. 
# The extra_args ensure that the x264 codec is used,
# so that the video can be embedded in html5. 

# ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

