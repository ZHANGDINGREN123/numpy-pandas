import theano
import theano.tensor as T
import random
import numpy

x = T.vector()
w = theano.shared(numpy.array([1., 1.]))#假设w初始值[1, 1]
b = theano.shared(0.)#假设b初始值[0]

z = T.dot(w, x) + b#z = w*a + b = (w1*x1+w2*x2+b) (向量积的运算+b)
y = 1/(1 + T.exp(-z))#Activation function

neuron = theano.function(
    inputs=[x],
    outputs=[y]
)

y_hat = T.scalar()
cost = T.sum((y - y_hat)**2)

dw, db = T.grad(cost, [w, b])

gradient = theano.function(
    inputs=[x, y_hat],
    outputs=[dw, db]
)

x = [1, -1]
y_hat = 1

for i in range(10000):
    print(neuron(x))
    dw, db = gradient(x, y_hat)
    w.set_value(w.get_value() - 0.1 * dw)
    b.set_value(b.get_value() - 0.1 * db)
    print(w.get_value(), b.get_value())
