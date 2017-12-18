# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:48:33 2017

@author: 93138
"""

from numpy import *
import matplotlib.pyplot as plt
def loadDataSet(fileName, delim='\t'):#导入数据集
    fr = open(fileName)#打开文件
    stringArr = [line.strip().split(delim) for line in fr.readlines()]#逐行读取数据，回车放入列表
    datArr = [map(float,line) for line in stringArr]
    return mat(datArr)#生成矩阵

def pca(dataMat, topNfeat=9999999):
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals #减去平均值
    covMat = cov(meanRemoved, rowvar=0)#求协方差矩阵
    eigVals,eigVects = linalg.eig(mat(covMat))#特征值，特征向量
    eigValInd = argsort(eigVals)            #索引从大到小排序
    eigValInd = eigValInd[:-(topNfeat+1):-1]  #留下部分特征值
    redEigVects = eigVects[:,eigValInd]       #对应的特征向量
    lowDDataMat = meanRemoved * redEigVects#将数据转化为低维空间
    reconMat = (lowDDataMat * redEigVects.T) + meanVals#重新构建数据
    return lowDDataMat, reconMat

def plotBestFit(dataSet1,dataSet2):  #加载数据集    
    dataArr1 = array(dataSet1) #转换成numpy中array
    dataArr2 = array(dataSet2)
    n = shape(dataArr1)[0] #数据的个数
    n1=shape(dataArr2)[0]
    xcord1 = []; ycord1 = []#正样本
    xcord2 = []; ycord2 = []#负样本
    xcord3=[];ycord3=[]
    j=0
    for i in range(n):
        
            xcord1.append(dataArr1[i,0]); ycord1.append(dataArr1[i,1])
            xcord2.append(dataArr2[i,0]); ycord2.append(dataArr2[i,1])
                   
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()    




if __name__=='__main__':
     mata=loadDataSet(r"C:\Users\93138\Desktop/testSet.txt")  
     a,b= pca(mata, 2)#PCA输入参数，参数一是输入数据集，参数二是提取的维数
     plotBestFit(a,b)