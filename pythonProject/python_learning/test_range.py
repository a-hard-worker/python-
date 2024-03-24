# for循环本质是遍历：序列类型（对象是字符串）
# range（num）  从0到num-1结束的数字序列
# range(num1,num2) 从num1到num2-1的数字序列
# range(num1,num2,step) 从num1到num2（不包含num2）的步长为step的数字序列
# range主要用于for循环控制次数时使用
"""num=int(input("请输入数字，统计从1到这个数字(不包括这个数字)中有多少个偶数"))
i=0
for x in range(1,num):
    if x%2==0:
        i+=1
print(i)"""

# continue跳过循环后面的语句，执行循环体内的下一次循环
# break直接跳出循环，执行循环后面的代码
# 两者都只是作用域其所在的循环