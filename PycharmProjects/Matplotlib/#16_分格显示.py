import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#method 1:subplot2grid
plt.figure(num=1)
#分为(3, 3)即3*3块,从(0, 0)开始,占3列1行
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
#对ax1绘制图像
ax1.plot([1, 2], [1, 2])
#设置标签
ax1.set_title('ax1_title')

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
ax2.plot([1, 2], [1, 2])

ax3 = plt.subplot2grid((3, 3), (1, 2), colspan=1, rowspan=2)
ax3.plot([1, 2], [1, 2])

ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=1, rowspan=1)
ax4.plot([1, 2], [1, 2])

ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1, rowspan=1)
ax5.plot([1, 2], [1, 2])


#method 2:gridspec
#共分为第0, 1, 2行与第0, 1, 2列
plt.figure(num=2)
gs = gridspec.GridSpec(3, 3)#设置3*3块
ax1 = plt.subplot(gs[0, :])#ax1占据第0行,‘：’表示所有列,即ax1占据第0行的所有3列
ax2 = plt.subplot(gs[1, :2])#ax2占据第1行,‘：2’表示前两列,即ax2占第据1行的前两列
ax3 = plt.subplot(gs[1:, 2])#ax3占据第1行后所有行，即占据1,2行,‘2’表示第两列,即ax3占第据1,2行的第2列
ax4 = plt.subplot(gs[2, 0])#ax4占据第2行,‘：0’表示第0列,即ax4占第据2行的第0列
ax5 = plt.subplot(gs[-1, -2])#ax5占据第2行,即-1行,‘-2’表示倒数第二列即第1列,所以ax5占第据2行的第1列

#method 3:easy to define structure
plt.figure(num=3)
#共享x,y轴
f,((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])#只划ax11


#plt.tight_layout()
plt.show()