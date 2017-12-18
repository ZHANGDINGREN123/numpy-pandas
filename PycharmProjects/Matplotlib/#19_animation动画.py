import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10))#10变大动画变慢
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

#frames=100:共100帧,interval=20:间隔20毫秒更新一次。blit=(False:整张图片都更新。True:只更新变化的值）
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False)
plt.show()