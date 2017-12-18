import theano
import theano.tensor as T

A = T.matrix()
B = T.matrix()

C = A * B
D = T.sum(C)

g = T.grad(D, A)#参考theano DNN.pdf第21页
#g_1 = T.grad(C, A)#不能用C进行偏微分,因为C不是变量而是矩阵.

y_prime = theano.function([A, B], g)

A = [[1, 2],
     [3, 4]]
B = [[2, 4],
     [6, 8]]

print(y_prime(A, B))