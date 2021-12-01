import matplotlib.pyplot as plt

# method 3: easy to define structure
####################################
fig, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])

fig.canvas.set_window_title('My Window Title') 
plt.tight_layout()
plt.show()