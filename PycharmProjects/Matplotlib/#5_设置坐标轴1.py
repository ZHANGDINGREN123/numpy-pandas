import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2


#以下内容定义figure12
plt.figure(num=12)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')#红色,线宽1.0,类型虚线
plt.plot(x, y2)

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)#x下标从第三行代码参数(-3, 3, 50)换为第18行代码参数(-1, 2, 5)

#更漂亮格式r'$内容$' 其中r表示正则表达式; '\ '表示空格 '\alpha'表示数学a(aerfa)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad\ \alpha$', 'normal', '$good$', 'really good'])

plt.show()