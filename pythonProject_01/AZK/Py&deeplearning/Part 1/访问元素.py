import numpy as np


'''
访问元素，下标从0开始
直接访问的方式如下：
'''

X = np.array([[51,55],[14,19],[0,4]])
# print(X)
# print(X[0])                 #打印矩阵的第一行
# print(X[0][1])              # （0，1）第一行第二列的元素值


#　用for语句的方式
for row in X:
    print(row)


# 使用数组访问各个元素
# X = X.flatten()     # 将X转化为一维数组
# print(X)
# print(X[np.array([0,2,4])])     # 获取索引为0，2，4的元素


# 从X中抽取大于15的元素
X = X.flatten()     # 将X转化为一维数组
print(X>15)
print(X[X>15])