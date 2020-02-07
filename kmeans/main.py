import json
import numpy as np
import random
import matplotlib.pyplot as plt

co=['red','darkorange','gold','green','deepskyblue','blue','violet','pink','black','cyan']
K = 10

def distance(sub1, sub2):
    result = sub1 - sub2  # numpy的数组可以对一个向量做减法，得到的还是一个向量
    return np.sqrt(np.sum(np.square(result)))  # 对向量做平方,求和,开方,得到sub1和sub2的欧式距离

def kmeans(centerArray,num):
    for i in range(num):
        mindis = 10000
        sub1 = x[i, :]  # 获取矩阵x的第i行数据
        for j in range(K):
            sub2 = centerArray[j, :]  # 按行读取质心列表中的行向量
            temp = distance(sub1, sub2)  # 逐个元素计算与质心的距离
            #print ("the disctent %f"%(temp))
            if (temp < mindis):  # 在k个质心里面选择距离最小的
                mindis = temp
                tempclass[i] = j  # 得到样本i 距离最近 质心

    print(tempclass)
    # 更新质心
    for j in range(K):  # 按照质心个数，统计每个质心下面的样本
        tempclassResult = x[tempclass == j]  # 从分类结果里面分别拿到每个类的样本
        x1 = np.mean(tempclassResult[:, 0])  # 取出tempclassResult里面第0列的值序列，并对这个序列计算均值
        x2 = np.mean(tempclassResult[:, 1])
        centerArray[j, :] = [x1, x2]  # 更新质心数组里面的质心坐标

with open("order1101_up_heat.json",'r') as load_f:
    load_dict = json.load(load_f)[0]

    n=len(load_dict)
    #n=1000
    x=np.zeros([n,2])
    for i in range(n):
        x[i,:] = load_dict[i]['coord']

    tempclass = np.zeros(x.shape[0])  # 获得x的第0列的维度
    center = random.sample(range(x.shape[0]), K)  # 从x的第0列数中随机挑选k个数
    centerArray = x[center, :]  # 从x中 获得以center的序列内容为行的向量，列数是从第0列到最后一列
    # 迭代100次
    for i in range(100):
        print("i=%d" % i)
        kmeans(centerArray,n)
    #for j in range(n):
        #plt.scatter(x[j,0],x[j,1],c=co[int(tempclass[j])],edgecolor='none',s=10)
        #plt.show()
    #for j in range(K):
        #plt.scatter(centerArray[j,0],centerArray[j,1],color=co[j],s=100)
    #plt.show()

    print(centerArray[:,:])