import numpy as np
A = np.arange(12).reshape((3,4))
print(A)
print(np.split(A, 2, axis=1))#对列分割成2块（只能等分）
print(np.split(A, 3, axis=0))#对行分割成3块（只能等分）
print('1################################')
print(np.array_split(A, 3, axis=1))#对列分割成3块（不等分）

print(np.vsplit(A, 3))#上下分割
print(np.hsplit(A, 2))#左右分割