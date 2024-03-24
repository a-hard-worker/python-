import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as pl
from sklearn.linear_model import LogisticRegression

# 读取txt文件中的数据

data=np.genfromtxt('D:\桌面\线性模型练习\逻辑回归\ex2data1.txt', delimiter=',')

# 从txt中读取的数据前两列为特征值向量
x=data[:,:2]
# 第三列为目标
y=data[:,2]

model=LogisticRegression()
model.fit(x,y)

# 绘图
plt.scatter(x[y==0][:,0],x[y==0][:,1],color='red',label='non-admitted')
plt.scatter(x[y==1][:,0],x[y==1][:,1],color='green',label='admitted')

# 绘制决策边界
# model.intercept_ 和 model.coef_:
# model.intercept_ 是逻辑回归模型的截距项。
# model.coef_ 是模型的系数数组，其中 model.coef_[0][0] 是第一门成绩的系数，model.coef_[0][1] 是第二门成绩的系数。
# np.dot 函数计算两个数组的点积。在这里，它将第一门成绩的系数与x轴的范围（x_values）相乘。

x_value=[np.min(x[:,0]),np.max(x[:,0])]
y_value=-(model.intercept_+np.dot(model.coef_[0][0],x_value))/model.coef_[0][1]
plt.plot(x_value,y_value,label='决策边界')
plt.xlabel('the first class-grade')
plt.ylabel('the second class-grade')

plt.show()
