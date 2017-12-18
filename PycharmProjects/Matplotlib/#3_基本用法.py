import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1, 1, 50)
y = 2 * x + 1
y1 = x ** 2
plt.figure(1)
plt.plot(x, y)
plt.figure(2)
plt.plot(x, y1)
plt.show()