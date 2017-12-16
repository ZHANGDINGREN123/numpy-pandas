import numpy as np
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
C = np.vstack((A, B))#上下合并(vertical-垂直)
D = np.hstack((A, B))#左右合并(horizon-水平)
print(A.shape, C.shape)
print(C)
print(A.shape, D.shape)
print(D)
print(A.T)#不能使用.T使得A矩阵从1*3变为3*1.(其他n*m可以转置为m*n)
print(C.shape)
print((C.T).shape)
print('#############以下展示如何解决‘不能使用.T’问题####################\n')
print(A[np.newaxis, :].shape)
print(A[np.newaxis, :])#从[1 1 1]变为[[1 1 1]]。(相当于行增加维度)

print(A[:, np.newaxis].shape)#使得A矩阵从1*3变为3*1.
print(A[:, np.newaxis])#使得A矩阵从1*3变为3*1.(相当于列增加维度)
print('2#################################\n')
A_T = np.array([1, 1, 1])[:, np.newaxis]#使得A_T矩阵从1*3变为3*1.
B_T = np.array([2, 2, 2])[:, np.newaxis]#使得B_T矩阵从1*3变为3*1.
print(A_T)
print(B_T)
E = np.hstack((A_T, B_T))#左右合并
print(E)
F = np.vstack((A_T, B_T))#上下合并
print(F)
print('3#################################\n')
G = np.concatenate((A, B, B, A), axis=0)#(A, B, B, A)左右合并（即横向合并）
print(G)
H = np.concatenate((A, B, B, A), axis=1)#(A, B, B, A)上下合并（即纵向合并）(正确，可能有些编译器通过不了)
print(H)
