# 函数
# print('小郑的身高是%f米'%1.75)
# print('小郑的体重是%f公斤'%75.2)
# print('小郑的爱好是%s'%"音乐")

# def printinf():
#     '''
#     这个函数用来输出个人信息
#     :return:
#     '''
#     print('小郑的身高是%f米' % 1.75)
#     print('小郑的体重是%f公斤' % 75.2)
#     print('小郑的爱好是%s' % "音乐")
#     pass
# printinf()#函数的调用


# 输出不同人的信息，方案：用参数解决
# def printinf(name,height,weight,hobby):
#     print('%s的身高是%f米' %(name,height))
#     print('%s的体重是%f公斤' %(name,weight))
#     print('%s的爱好是%s' % (name,hobby))
#     pass
# printinf("小郑",1.75,70.6,"音乐")
# printinf("小老虎",1.65,50,'吃零食')


# 参数的分类
# 必选参数、默认参数、可选参数、关键字参数
# def sum(a,b):
#     sum=a+b
#     print(sum)
#     pass
# #函数调用
# sum(3,2)
# sum(80,20)

# def insum(a=12,b=18):'''默认参数的使用'''
#     he=a+b
#     print(he)
#     pass
# insum()
# insum(13,19)


# 可变参数的使用，参数个数不确定时使用
# def getshuju(*args):
#     '''
#     计算累加和
#     :param args: 可变长的参数类型
#     :return:
#     '''
#     sum=0
#     for i in args:
#         sum+=i
#         pass
#     print('sum=%d'%sum)
#     pass
# getshuju(2,3)
# getshuju(1,2,3,4,5,6,7,8,9,10)

# 关键字参数，是一个字典类型，其key是字符串，用**来定义
# def keyeee(**kwargs):
#     print(kwargs)
#     pass
# dictA={"name":'xiaolaohu',"age":20}
# keyeee(**dictA)

# 关键字参数的应用
# def functioncc(*args,**kwargs):
#     '''
#     可选参数必须放到关键字可变参数之前
#     :param args:
#     :param kwargs:
#     :return:
#     '''
#     print(args)
#     print(kwargs)
#     pass
# functioncc(1,1,2,name='cxq')
# functioncc(age=21)

# 函数返回值,return后面的代码不会执行
# def sum(a,b):
#     sum=a+b
#     return sum
#     pass
# rs=sum(12,18)
# print(rs)

# 计算累加和的函数执行
# def ljia(num):
#     result=0
#     i=0
#     while i<=num:
#         result+=i
#         i+=1
#         pass
#     return result
# pass
# daan=ljia(100)
# print(daan)

# 返回元组
# def tes():
#     return 1,2,3
# q=tes()
# print(q)

# def di():
#     '''
#     返回字典
#     :return:
#     '''
#     return {"name": 'zhengkui&cxq'}
#     pass
# test1=di()
# print(test1)

# def li():
#     '''
#     返回列表
#     :return:
#     '''
#     return [0,0,7]
#     # return (1,1,9)#元组类型加不加小括号都是一样的
# test_1=li()
# print(test_1)
# print(type(test_1))


# 函数嵌套
# def fun_1():
#     print("xiaolaohu")
#     pass
# def fun_2():
#     fun_1()
#     print(520)
#     pass
# fun_2()
