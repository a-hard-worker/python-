import random
sum=10000
for i in range(1,21):
    num=random.randint(1,10)
    if sum<=0:
        print("工资发完了，请下个月再领取")
        break
    else:
        if num<5:
            print(f"员工{i}，绩效分{num},低于5，不发工资,下一位")
            continue
        else:
            sum-=1000
            print(f"向员工{i}发放工资1000元，账户余额还有{sum}元")
            continue
