import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)
y = 1/(1 + np.exp(-x))
z = np.polyfit(x,y,3)#用三次多项式拟合
p = np.poly1d(z)
print(p)
yvals = p(x)
plot1 = plt.plot(x, y, '*', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)
plt.title('polyfitting')
plt.show()