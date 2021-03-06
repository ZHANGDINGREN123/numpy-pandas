import theano
import theano.tensor as T
x1 = T.scalar()
x2 = T.scalar()

y = x1 * x2
g = T.grad(y, [x1, x2])#g = [dy/dx1,dy/dx2] = [x2, x1] !!(不会写偏导符号)

f = theano.function([x1, x2], y)
f_prime = theano.function([x1, x2], g)

print(f(2, 4))
print(f_prime(2, 4))