import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import pylab as pl

x = np.linspace(0, 10, 11)
y = np.sin(x)
xnew = np.linspace(0, 10, 101)
pl.plot(x, y, "ro")

for kind in ["nearest", "zero", "slinear", "quadratic", "cubic"]:
    #"nearest","zero"为阶梯插值
    #"slinear"为线性插值
    #"slinear", "cubic"为2阶,3阶样条曲线插值
    f = interpolate.interp1d(x, y, kind = kind)
    ynew = f(xnew)
    pl.plot(xnew, ynew, label = str(kind))
pl.legend(loc = "lower right")

plt.show()


