# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:24:51 2017

@author: 93138
"""

import numpy as np
# n维的原始数据，本例中n=2。
data = np.array([[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0], [2.3, 2.7],\
                 [2, 1.6], [1, 1.1], [1.5, 1.6], [1.1, 0.9]])
print data
# (1)零均值化
def zeroMean(dataMat):
    # 求各列特征的平均值
    meanVal = np.mean(dataMat, axis=0)#按列求均值
    newData = dataMat - meanVal
    return newData, meanVal
newData, meanVal = zeroMean(data)
print 'the newData is \n', newData
print 'the meanVal is \n', meanVal
covMat = np.cov(newData, rowvar=0)#求协方差
print covMat
eigVals, eigVects = np.linalg.eig(np.mat(covMat))#求特征值，特征向量
print '特征值为：\n', eigVals
print '特征向量为\n', eigVects
eigValIndice = np.argsort(eigVals) # 从小到大排序
n_eigValIndice = eigValIndice[-1:-(1+1):-1] # 取值最大的k个下标
n_eigVect = eigVects[:, n_eigValIndice] # 取对应的k个特征向量
print n_eigVect
print n_eigVect.shape
lowDataMat = newData*n_eigVect # 低维特征空间的数据
reconMat = (lowDataMat * n_eigVect.T) + meanVal # 重构数据，得到降维之后的数据
print '将样本点投影到选取的低维特征向量上,实际使用的是这个结果作为新的特征：\n', lowDataMat
print '降维之后的样本:\n', reconMat