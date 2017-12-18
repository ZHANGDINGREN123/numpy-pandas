import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import theano.tensor as T
import theano
import random
from random import shuffle
img_count = 0
def showimg(img):
    muki_pr = np.zeros((500,500,3))
    l = img.tolist()
    count = 0
    for x in range(500):
        for y in range(500):
            muki_pr[y][x] = l[count]
            count += 1
    plt.imshow(muki_pr)

def saveimg(fname,img):
    muki_pr = np.zeros((500,500,3))
    l = img.tolist()
    count = 0
    for x in range(500):
        for y in range(500):
            muki_pr[y][x] = l[count]
            count += 1
    plt.imsave(fname,muki_pr)

def read_muki():
    img_data = np.random.randn(250000, 1)
    xy_data = []
    import random

    f = open('./muki.txt', 'rb')
    count = 0
    for line in f:
        y, x, c = line.split()
        xy_data.append([float(x), float(y)])
        x = (float(x)) * 100. + 250
        y = (float(y)) * 100. + 250
        c = float(c)

        img_data[count] = c

        count = count + 1
    return np.matrix(xy_data), img_data


xy_data, img_data = read_muki()
showimg(img_data)

# MUKI_NN
batch_size = 500
hidden_size = 128

x = T.matrix(name='x',dtype='float32') # size =2
y = T.matrix(name='x',dtype='float32') # size =1


w1 = theano.shared(np.random.randn(hidden_size,2))
b1 = theano.shared(np.random.randn(hidden_size))
w2 = theano.shared(np.random.randn(hidden_size,hidden_size))
b2 = theano.shared(np.random.randn(hidden_size))
w3 = theano.shared(np.random.randn(1,hidden_size))
b3 = theano.shared(np.random.randn(1))

#第一层
z1 = T.dot(w1, x) + b1.dimshuffle(0, 'x')
a1 = 1/(1+T.exp(-z1))
fa1 = theano.function(inputs=[x],
                      outputs=[a1],
                      allow_input_downcast=True)
l1_o = fa1(np.random.randn(2, batch_size))
l1_o = fa1(xy_data[:500].T)

#第二层
z2 = T.dot(w2, a1) + b2.dimshuffle(0, 'x')
a2 = 1/(1+T.exp(-z2))
fa2 = theano.function(inputs=[x], outputs=[a2], allow_input_downcast=True)
l2_o = fa2(np.random.randn(2, batch_size))
l2_o= fa2(xy_data[:500].T)
print(l2_o[0].shape)

#第三层
z3 = T.dot(w3,a2) + b3.dimshuffle(0,'x')
a3 = 1/(1+T.exp(-z3))
fa3 = theano.function(inputs=[x],outputs=[a3],allow_input_downcast=True)
l3_o = fa3(np.random.randn(2,batch_size))
print(l3_o[0].shape)

#定义cost function & update function
y_hat = T.matrix('reference',dtype='float32')
cost = T.sum((a3-y_hat)**2)/batch_size
dw1,dw2,dw3,db1,db2,db3 = T.grad(cost,[w1,w2,w3,b1,b2,b3])

def Myupdates(ps, gs):
    r = 0.5
    # pu = [(p, p - r * g) for p, g in izip(ps, gs)]
    pu = [(p, p - r * g) for p, g in zip(ps, gs)]
    return pu
train = theano.function(inputs=[x,y_hat],
                        outputs=[a3,cost],
                        updates=Myupdates([w1,w2,b1,b2,w3,b3],[dw1,dw2,db1,db2,dw3,db3]),
                        allow_input_downcast=True,)

#traing
def training(xy_data,img_data):
    for ii in range(1000):
        for i in range(500):

            start = i * 500
            end  = start + 500
            img_predict,cost_predict = train(xy_data[start:end].T,img_data[start:end].T)

        if ii % 5 == 0:
            saveimg('./imgs/muki_'+ str(ii) +'.png', fa3(xy_data.T)[0].T)
        print(cost_predict,)
training(xy_data,img_data)

#traing-random suffule
all_data = zip(xy_data,img_data)
shuffle(all_data)
temp_xy = []
temp_data = []
for row in all_data:
    temp_xy.append(row[0].tolist()[0])
    temp_data.append(row[1])
s_data = np.matrix(temp_data)
s_xy = np.matrix(temp_xy)

#testing
showimg(fa2(xy_data.T)[0].T)