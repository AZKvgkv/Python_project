# for 循环
# tags = '你当像鸟飞往你的山'
# for i in tags:
#     print(i)
#     pass

# range 动态生成一个函数对象，生成一个函数列表；（起始，结束，步长）------【起始，结束）
# sum = 0
# for data in range(1,101):
#     sum +=data
#     # print(data,end=' ')
#     pass
# print("sum=%i "%sum)
# for data in range(10,101):
#     if data % 2 == 0:
#         print("%i是偶数"%data)
#         pass
#     else:
#         print("%i是奇数"%data)
#         pass
#     pass
# sum = 0
# for it in range(1,21):
#     if sum>70:
#         print("循环执行到%i就结束了"%it)
#         break
#         pass
#     sum+=it
#     pass
# print("sum=%d"%sum)
# for item in range(1,16):
#     if item%2==0:
#         continue
#         pass
#     print(item)




# for 循环嵌套，99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end=' ')
#         pass
#     print()
#     pass

# for item in range(1,11):
#     print(item,end=' ')
#     if item>=8:
#         break
#     pass
# else:
#     print("已经执行完了吗？")
#     pass


# 模拟登录
# account = "az088678771"
# password = "088678771"
# for i in range(3):
#     zh = input('请输入您的账号：')
#     mm = input('请输入您的密码：')
#     if account==zh and password==mm:
#         print('恭喜您输入正确，登录成功')
#         break
#         pass
#     else:
#         print('您的账号或密码输入错误，请检查后再次输入')
#     pass
# else:
#     print('您已三次未正确输入，因此被锁定15min')


# 作业1
# times = 0
# count = 3
# while times<=3:
#     age = int(input('请输入年龄：') )
#     if age==22:
#         print("恭喜您，猜对了！")
#         break
#         pass
#     elif age>22:
#         print("很遗憾，您猜大了")
#         pass
#     else:
#         print("很遗憾，您猜小了")
#         pass
#     times+=1
#     if times==3:
#         choose=input('想不想继续呢（Y/N）？')
#         if choose=='Y'or choose=="y":
#             times=0
#             pass
#         elif choose=='N'or choose=="n":
#             times==4
#             print('本次游戏到此结束')
#             break
#             pass
#         else:
#             print('请按要求输入')
#         pass
#     pass
#

# 作业2,计算BMI的值
# high =float(input("请输入您的身高："))
# weight =float(input('请输入您的体重：'))
# bmi=weight/(high**2)
# print("BMI的数值%f"%bmi)
# if bmi<18.5:
#     print("您的身材过轻")
#     pass
# elif bmi<25:
#     print("您的身材正常，棒棒哒！")
#     pass
# elif bmi<28:
#     print("您的身材过重")
#     pass
# elif bmi<32:
#     print("您的身材肥胖")
#     pass
# else:
#     print("您的身材严重肥胖")
#     pass
#
