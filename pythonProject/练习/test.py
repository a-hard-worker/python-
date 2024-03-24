import numpy as np

"""
函数说明:sigmoid函数
Parameters:
    inX - 数据
Returns:
    sigmoid函数
"""


def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))


"""
函数说明：改进的随机梯度上升算法
Parameters:
    dataMatrix - 数据数组
    classLabels - 数据标签
    numIter - 迭代次数
Returns:
    weights - 球的的回归系数数组(最优参数)
"""


def stocGradAscent1(dataMatrix, classLabels, numIter):
    m, n = np.shape(dataMatrix)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4.0 / (j + i + 1.0) + 0.01
            randIndex = int(np.random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(weights * dataMatrix[dataIndex[randIndex]]))
            error = classLabels[dataIndex[randIndex]] - h
            weights = weights + alpha * error * dataMatrix[dataIndex[randIndex]]
            del (dataIndex[randIndex])
    return weights


"""
函数说明:计算对应的sigmoid值
Parameters:
    inX - 数据
    weights - 回归系数
Returns:
    1/0
"""


def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0


"""
函数说明：打开训练集和测试集，并对数据进行格式化处理
Parameters:
    无
Returns:
    errorRate - 错误率
"""


def colicTest():
    frTrain = open('horseColicTraining.txt', 'r')
    frTest = open('horseColicTest.txt', 'r')
    # 训练模型
    trainingSet = [];
    trainingLabels = []
    for line in frTrain.readlines():
        currntLine = line.strip().split('\t')
        lineArry = []
        for i in range(len(currntLine) - 1):
            lineArry.append(float(currntLine[i]))
        trainingSet.append(lineArry)
        trainingLabels.append(float(currntLine[-1]))
    trainingWeights = stocGradAscent1(np.array(trainingSet), trainingLabels, 500)
    # 测试模型
    errorCount = 0;
    numTest = 0.0
    for line in frTest.readlines():
        numTest += 1.0
        currntLine = line.strip().split('\t')
        lineArry = []
        for i in range(len(currntLine) - 1):
            lineArry.append(float(currntLine[i]))
        if int(classifyVector(np.array(lineArry), trainingWeights)) != int(currntLine[-1]):
            errorCount += 1
    errorRate = float(errorCount / numTest) * 100
    print('分类错误率：%.2f%%' % errorRate)
    return errorRate


"""
函数说明：调用函数colicTest()10次并求结果的平均值
Parameters:
    无
Returns:无
"""


def muliTest():
    numTests = 10;
    errorSum = 0.0
    for i in range(numTests):
        errorSum += colicTest()
    errorAverage = errorSum / numTests
    print("10次测试结果的平均值:%.2f%%" % errorAverage)


muliTest()