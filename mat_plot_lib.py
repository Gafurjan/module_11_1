import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots(facecolor=(.18, .31, .31))             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 1], [1, 4, 2, 1])  # Plot some data on the Axes.
# # plt.show()                           # Show the figure.
#
# # fig = plt.figure()             # an empty figure with no Axes
# fig, ax = plt.subplots(facecolor=(.18, .31, .31))       # a figure with a single Axes
# fig, axs = plt.subplots(2, 2, facecolor=(.18, .31, .31))  # a figure with a 2x2 grid of Axes
# # a figure with one Axes on the left, and two on the right:
# fig, axs = plt.subplot_mosaic([['left', 'right_top'],
#                                 ['left', 'right_bottom']])
#
# plt.show()


# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10 Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)

cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Coherence')

plt.show()