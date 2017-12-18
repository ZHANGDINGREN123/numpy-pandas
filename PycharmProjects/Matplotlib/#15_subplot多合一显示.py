import matplotlib.pyplot as plt
import numpy as np

plt.figure()

#将整个figure分成2行，其中第一行有一列, 现在绘制第一个图块
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

#将整个figure分成2行，其中第二行有三列, 现在绘制第四个图块
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])

#将整个figure分成分成2行，其中第二行有三列, 现在绘制第五个
plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])

#将整个figure分成分成2行，其中第二行有三列, 现在绘制第六个
plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 4])



plt.show()