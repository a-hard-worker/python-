# while循环语句
# 语法：
# while 布尔表达式：
#       要执行的语句
# 例子
import random
num = random.randint(1,100)
i=0
# 用flag做布尔变量，猜对后将flag设置为False即终止
flag=True
while flag:
    guess_num = int(input("请输入你猜的数字"))
    if guess_num>num:
        print("猜大了")
        i+=1
    elif guess_num<num:
        print("猜小了")
        i+=1
    else:
        print(f"猜对了，这个数是{num}，你共使用了{i}次机会")
        flag=False
