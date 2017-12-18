import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8,5))
plt.plot(x, y)#1:绘出连续线段
#plt.scatter(x, y)#2:绘出离散点点

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=50, color='b')#大小50,颜色蓝色
plt.plot([x0, x0], [y0, 0], 'k--', lw = 2.5)#'k'表示黑色,'--'表示虚线,lw表示线宽,绘出(x0,y0)(x0,0)的线

#################################
#method 1
plt.annotate(r'$2x+1=3$',xy = (x0, y0), xycoords = 'data',xytext = (+30,-30),#xycoords指箭头指向(x0,y0)
             #xytext指2x+1=3显示在箭头尾部(+30,-30)位置
             textcoords='offset points',
             #arrowstyle='->'：箭头类型
             #connectionstyle='arc3,rad=.2'：箭头弧度及角度
             fontsize = 16, arrowprops = dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

################################
#method 2
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',#-3.7,3表示文本位置
         fontdict={'size':16, 'color':'r'})


plt.show()