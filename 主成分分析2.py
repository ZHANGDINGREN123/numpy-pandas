# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:19:21 2017

@author: 93138
"""

import numpy as np
# n维的原始数据，本例中n=2。
data = np.array([[2.5,2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0], [2.3, 2.7],\
                 [2, 1.6], [1, 1.1], [1.5, 1.6], [1.1, 0.9]])
print data
def zeroMean(dataMat):
    # 求各列特征的平均值
    meanVal = np.mean(dataMat, axis=0)#按列求均值
    newData = dataMat - meanVal
    return newData, meanVal
def pca(dataMat,percentage=0.85):
    newData,meanVal=zeroMean(dataMat)
    covMat=np.cov(newData,rowvar=0)    #求协方差矩阵,return ndarray；若rowvar非0，一列代表一个样本，为0，一行代表一个样本
    eigVals,eigVects=np.linalg.eig(np.mat(covMat))#求特征值和特征向量,特征向量是按列放的，即一列代表一个特征向量
    n=percentage2n(eigVals,percentage)                 #要达到percent的方差百分比，需要前n个特征向量
    eigValIndice=np.argsort(eigVals)            #对特征值从小到大排序
    n_eigValIndice=eigValIndice[-1:-(n+1):-1]   #最大的n个特征值的下标
    n_eigVect=eigVects[:,n_eigValIndice]        #最大的n个特征值对应的特征向量
    lowDDataMat=newData*n_eigVect               #低维特征空间的数据
    reconMat=(lowDDataMat*n_eigVect.T)+meanVal  #重构数据
    return lowDDataMat,reconMat
print '将样本点投影到选取的低维特征向量上,实际使用的是这个结果作为新的特征：\n', lowDataMat
print '降维之后的样本:\n', reconMat