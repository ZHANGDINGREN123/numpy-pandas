# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 19:37:41 2017

@author: admin
"""

import numpy as np
import operator

def createDataSet():#创建一个新的数据集
    group=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])#4个样本2个类
    labels=['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):#定义一个KNN分类
    dataSetSize=dataSet.shape[0]#样本大小等于数据集的行数 即有4个样本 shape[0]表示行数
    diffMat=np.tile(inX,(dataSetSize,1))-dataSet#tile数组沿各维度重复自己
    print diffMat
    # 开始计算欧氏距离
    ddMat=diffMat**2
    dsumMat=np.sum(ddMat,axis=1)#按行求和
    deqrMat=dsumMat**0.5
    #对距离进行排序
    sortMat=deqrMat.argsort()#argsort函数返回的是数组值从小到大的索引值
    dic={}#定义一个字典
    for i in range(k):
        lab=labels[sortMat[i]]#选择距离K
        dic[lab]=dic.get(lab,0)+1#计算出现的标签次数，当标签次数不在字典中时，获取/输出
    maxlabelcout=sorted(dic.iteritems(),key=operator.itemgetter(1),reverse=True)#选出最大的类别数,
    #operator.itemgetter函数获取的不是值，而是定义了一个函数，表示sort将按照第2个域的值排序，通过该函数作用到对象上才能获取值。reverse参数为True时将按降序排列。
    return maxlabelcout[0][0]    #返回最大的类别


from sklearn import neighbors,datasets
group,labels=createDataSet()
print group
print labels
g=classify0([0,0],group,labels,3)
print g
# help(operator)