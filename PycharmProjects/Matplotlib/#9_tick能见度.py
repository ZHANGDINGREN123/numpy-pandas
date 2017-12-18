import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3, 3, 50)
y1 = 0.1 * x

#以下内容定义figure12
plt.figure()
plt.plot(x, y1, linewidth=10.0)

plt.ylim((-2, 2))

ax = plt.gca()#gca = 'get current axis'取得当前轴线
ax.spines['right'].set_color('none')#去掉右边界轴线
ax.spines['top'].set_color('none')#隐藏上边界轴线
ax.xaxis.set_ticks_position('bottom')#用下边界轴线作为x轴
ax.yaxis.set_ticks_position('left')#用左边界轴线作为y轴
ax.spines['bottom'].set_position(('data', -0))#x轴(下轴线)放在y轴(左轴线)值为0的点处('data' or 'outward' or 'axes')
ax.spines['left'].set_position(('data', 0))#y轴(左轴线)放在x轴(下轴线)值为0的点处

for label in ax.get_xticklabels() + ax.get_yticklabels():
    #set_fontsize(12)：字体大小
    label.set_fontsize(12)
    #facecolor:背景颜色. edgecolor：边框颜色. alpha：透明度.
    label.set_bbox(dict(facecolor='red', edgecolor='green',alpha=0.7))


plt.show()