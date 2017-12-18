import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

#以下内容定义figure11
plt.figure(num=11,figsize=(8,5))
plt.plot(x, y1)

#以下内容定义figure12
plt.figure(num=12)
plt.plot(x, y1, color='red', linewidth=10.0, linestyle='--')#红色,线宽1.0,类型虚线
plt.plot(x, y2)

plt.show()