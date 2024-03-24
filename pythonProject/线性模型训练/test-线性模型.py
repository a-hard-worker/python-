import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt("D:\桌面\线性模型练习\线性回归\ex1data1.txt",delimiter=',')
# 提取txt文件中的第一列和第二列的数据
x=data[:,0]
y=data[:,1]

x=np.stack([np.ones(x.shape[0]),x],axis=1)
# 初始化参数,y=ax+b
a=0
b=0

# 定义学习率和迭代次数
"""learning_rate = 0.01
iterations = 1500"""
learning_rate=float(input("请您输入学习率"))
iterations=int(input("请您输入迭代次数"))

# 采用梯度下降的方法
for _ in range(iterations):
    # 计算得出预测值
    prediction=x.dot([b,a])
    # 计算得到误差
    error=prediction-y
    # 更新参数，同步更新
    b-=learning_rate * np.sum(error) /len(x)
    a-=learning_rate * np.dot(error,x[:,1]) /len(x)

# 绘图
plt.scatter(x[:,1],y,color='red',marker='x',label='训练数据')
plt.plot(x[:,1],x.dot([b,a]),color='green',label='线性回归线')
plt.xlabel('城市人口数（万）')
plt.ylabel('餐馆利润（万美元）')
plt.title('线性回归')
plt.legend()
plt.show()

print(f"梯度下降法得到的参数：a={a}，b={b}")