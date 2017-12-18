import theano
import theano.tensor as T
x = theano.tensor.scalar()
y = x ** 2
f = theano.function([x], y)
print(f(-2))

a = T.scalar()
b = T.matrix()
c = T.matrix('ha ha ha')
print(a)
print(b)
print(c)