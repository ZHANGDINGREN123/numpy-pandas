import theano
import theano.tensor as T
import random
import numpy

x = T.vector()
w1 = theano.shared(numpy.random.rand(2))
b1 = theano.shared(numpy.random.rand(1))
w2 = theano.shared(numpy.random.rand(2))
b2 = theano.shared(numpy.random.rand(1))
w = theano.shared(numpy.random.rand(2))
b = theano.shared(numpy.random.rand(1))
#w = theano.shared(numpy.array([1., 1.]))#假设w初始值[1, 1]
#b = theano.shared(1.)#假设b初始值[0]

a1 = 1/(1 + T.exp(-1 * (T.dot(w1, x) + b1)))#Activation function
a2 = 1/(1 + T.exp(-1 * (T.dot(w2, x) + b2)))
y = 1/(1 + T.exp(-1 * (T.dot(w, [a1, a2]) + b)))

y_hat = T.scalar()
cost = -(y_hat * T.log(y) + (1 - y_hat) * T.log(1 - y)).sum()

dw, db, dw1, db1, dw2, db2 = T.grad(cost, [w, b, w1, b1, w2, b2])

def MyUpdate(paramters, gradients):
    mu = 0.01
    paramters_updates = \
    [(p, p - mu *g) for p, g in zip(paramters, gradients)]
    return paramters_updates


gradient = theano.function(
    inputs=[x, y_hat],
    outputs=[y, cost],
    updates=MyUpdate([w, b, w1, b1, w2, b2], [dw, db, dw1, db1, dw2, db2])#update parameters
)


for i in range(100000):
    y1, c1 = gradient([0, 0], 0)
    y2, c2 = gradient([0, 1], 1)
    y3, c3 = gradient([1, 0], 1)
    y4, c4 = gradient([1, 1], 0)
    print(c1 + c2 + c3 + c4)
    print(y1, y2, y3, y4)
