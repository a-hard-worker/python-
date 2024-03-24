num=100

def l1():
    global count
    count: int=1
    print(num)

def l2():
    # global关键字可以在函数体内对外部变量进行操作
    global num
    num=300
    print(num)
l1()
l2()
print(num)
print(count)