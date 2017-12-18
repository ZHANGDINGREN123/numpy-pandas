import theano
import theano.tensor as T
x = T.scalar('x')
y = x ** 2
g = T.grad(y, x)#g = dy/dx = 2x

f = theano.function([x], y)
f_prime = theano.function([x], g)

print(f(-2))
print(f_prime(-2))