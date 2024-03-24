#生成随机int数
import random
num = random.randint(1,10)

input_num1 = int(input("请你输入猜测的结果："))
if input_num1>num:
    print("大了")
    input_num2=int(input("请你重新输入："))
    if input_num2>num:
        print("大了")
        input_num3 = int(input("请你重新输入："))
        if input_num3>num:
            print("没猜出")
        elif input_num3==num:
            print("猜出了")
        else:
            print("没猜出")
    elif input_num2<num:
        print("小了")
        input_num4 = int(input("请你重新输入："))
        if input_num4 > num:
            print("没猜出")
        elif input_num4 == num:
            print("猜出了")
        else:
            print("没猜出")
    else: print("猜出了")
elif input_num1<num:
    print("小了")
    input_num5 = int(input("请你重新输入："))
    if input_num5 > num:
        print("大了")
        input_num6 = int(input("请你重新输入："))
        if input_num6 > num:
            print("没猜出")
        elif input_num6 == num:
            print("猜出了")
        else:
            print("没猜出")
    elif input_num5 < num:
        print("小了")
        input_num7 = int(input("请你重新输入："))
        if input_num7 > num:
            print("没猜出")
        elif input_num7 == num:
            print("猜出了")
        else:
            print("没猜出")
    else:
        print("猜出了")
else:print("猜出了")

