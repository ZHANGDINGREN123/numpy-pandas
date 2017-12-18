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

print(w.get_value())
w.set_value([0., 0.])

for i in range(100):
    x = [random.random(), random.random()]
    print(x)
    print(neuron(x))
