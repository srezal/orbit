import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

center = 0
ta = np.arange(-2*np.pi, 2*np.pi, 0.01)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax_e_slide = plt.axes([.22, .9, .2, .03])
ax_r_0_slide = plt.axes([.22, .94, .2, .03])
e_slider = Slider(ax_e_slide, "e", valmin=0, valmax=3.0, valinit=0, valstep=0.1)
r_0_slider = Slider(ax_r_0_slide, "r_0", valmin=0.1, valmax=30.0, valinit=0.1, valstep=0.1)


def draw():
    e = e_slider.val
    r_0 = r_0_slider.val
    p = r_0*(1 + e)
    if (1 - e) > 0:
        r_a = p/(1 - e)
        a = p/(1 - e)
        b = math.sqrt(p*a)
        ax.set(xlim=(-b - 1, b + 1), ylim=(-r_a-1, r_0+1))
    else:
        ax.set(xlim=(-r_0 * 4, r_0 * 4), ylim=(-r_0 * 4, r_0 * 4))
    r = (r_0*(1 + e))/(1+(e*np.cos(ta)))
    x = r * np.sin(ta)
    y = r * np.cos(ta)
    y = np.ma.masked_greater(y, r_0)
    ax.plot(x, y, color='r')
    ax.scatter(center, center, color='k', marker='+')
    ax.set_xlabel('AU')
    ax.set_ylabel('AU')


def update(val):
    ax.clear()
    draw()


def run():
    draw()
    e_slider.on_changed(update)
    r_0_slider.on_changed(update)
    plt.show()
