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

ax = plt.gca()#gca = 'get current axis'取得当前轴线
ax.spines['right'].set_color('none')#去掉右边界轴线
ax.spines['top'].set_color('none')#隐藏上边界轴线
ax.xaxis.set_ticks_position('bottom')#用下边界轴线作为x轴
ax.yaxis.set_ticks_position('left')#用左边界轴线作为y轴
ax.spines['bottom'].set_position(('data', -1))#x轴(下轴线)放在y轴(左轴线)值为-1的点处('data' or 'outward' or 'axes')
ax.spines['left'].set_position(('data', 0))#y轴(左轴线)放在x轴(下轴线)值为0的点处

plt.show()