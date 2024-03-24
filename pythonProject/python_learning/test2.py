num=100
avg_score=98
print("这个班级有%s人，他们的平均分数是%s分"%(num,avg_score))
# %s代表占位字符串; %d占位整数; %f占位浮点数
# 占位符输出

# 格式化数值精度的控制 %m.nd  m为宽度 n为精度
float_s=15.226
str_a="asdffgh"
print("%5.4f"%float_s)


print(f"{str_a}+{float_s}")
# 使用{}大括号原样输出数据，格式为：f"{}+{可以是表达式}..."


