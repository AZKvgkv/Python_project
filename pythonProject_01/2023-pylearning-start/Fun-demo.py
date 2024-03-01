def add(a,b,c):
    '''
    :param a: 参数1
    :param b: 参数2
    :param c: 参数3
    :return: 3个参数的代数和
    '''
    sum = a + b + c
    return sum

print(add(10,15,19))



# lambda 表达式 和 匿名函数

f = lambda a,b,c : a + b + c
print(f(1,2,3))


g = [lambda a : a * 2,lambda b : b * 3,lambda c : c * 4]
print(g[2](3))
print(g[1](5))
print(g[0](6))



# 计算阶乘

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    pass


res = factorial(4)
print(f"4! = ",res)



# 嵌套函数

def outter():
    print('outter running!!!')

    def inner():
        print('inner running!!')


# 函数调用
outter()



# 嵌套函数的练习
def printName(isChinese, name, familyName):
    def inner_print(a, b):
        print('{0} {1}'.format(a,b))
    if isChinese:
        inner_print(familyName, name)
    else:
        inner_print(name, familyName)

printName(True,'奎', '郑')

