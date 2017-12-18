import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

#从底部和左部10%的位置开始作为坐标(0,0)点,坐标轴长宽占figure的80%
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
#设置主图
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

#从底部60%和左部20%的位置开始作为坐标(0,0)点,坐标轴长宽占figure的25%
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
#设置图中图
ax2.plot(y, x, 'b')#数据反过来
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

#从底部20%和左部60%的位置开始作为坐标(0,0)点,坐标轴长宽占figure的25%
#换一种方法表示

plt.axes([0.6, 0.2, 0.25, 0.25])
#将y的值逆序做图
plt.plot(y[::-1], x, 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')



plt.show()