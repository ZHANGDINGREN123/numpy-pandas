import matplotlib.pyplot as plt
import numpy as np

#image data
a = np.array([0.312321321, 0.364323213, 0.423721233,
              0.634232132, 0.631232344, 0.232132421,
              0.434123213, 0.645324123, 0.845324234]).reshape(3, 3)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')#
plt.colorbar(shrink=0.9)#颜色条

#去除坐标轴上的数
plt.xticks(())
plt.yticks(())

plt.show()