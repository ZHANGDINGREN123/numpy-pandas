import theano
import theano.tensor as T
import random

x = T.vector()
w = T.vector()
b = T.scalar()

z = T.dot(w, x) + b#z = w*a + b = (w1*x1+w2*x2+b) (向量积的运算+b)
y = 1/(1 + T.exp(-z))#Activation function

neuron = theano.function(
    inputs=[x, w, b],
    outputs=[y]
)

w = [-1, 1]#假设已知
b = 0#假设已知

for i in range(100):
    x = [random.random(), random.random()]
    print(x)
    print(neuron(x, w, b))
