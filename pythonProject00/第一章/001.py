# print('hello python')
# a = 20
# a = a+1
# print(type(a))
# b = ()
# # print(type(b))
# c = []
# print(type(c))
# d = {}
# print(type(d))
# 输出 %为占位符
# s--字符串；d/i--有符号的十进制整数
# name = "曹媛"
# aclass = "中心小学4年级2班"
# _age = 10
# print('我的名字：%s;来自【%s】;今年%d岁'%(name,aclass,_age))
# print("我是个\n聪明人")# \n表示换行
# 输出也可以用.format表示
# print("姓名：{}".format(name))



# 输入用input,获取键盘输入的内容，注意全是str类型
# name = input("请输入你的姓名:")
# QQ = input('请输入你的QQ号：')
# phone = input('请输入你的电话号：')
# print('姓名:{}\n年龄:{}'.format(name,20))
# print("QQ号：{}".format(QQ))
# print("电话号：{}".format(phone))
# age = int(input('请输入你的年龄：'))
# print('年龄为%i岁'%age)
# 单分支
# score = 50
# if score <=60:
#     print('成绩不合格')
#     pass#空语句
# print('语句运行结束')
# 双分支
# score = 46
# if score >60:
#     print('成绩合格')
#     pass
# else :
#     print("成绩不理想")
#     pass
# 多分支
# s = int(input("请输入你的分数:"))
# if s <60:
#     print("成绩不及格")
#     pass
# elif s <80:
#     print("成绩良好")
#     pass
# else:
#     print("成绩优秀")



# 猜拳游戏
# 0:石头；1:剪刀；2:布
# import random # 直接导入产生随机数的模块
# person = int(input('请出拳：[0:石头；1:剪刀；2:布]'))
# auto = random.randint(0,2)
# if person == 0 and auto == 1 or person == 1 and auto == 2 or person == 2 and auto == 0:
#     print('真棒，你赢了')
#     pass
# elif person == auto:
#     print("你们打了个平手")
# else:
#     print("很遗憾，你输了")
#     pass


# # if-else 的嵌套使用
# xuefen = int(input('请输入你的学分：'))
# if xuefen > 16:
#     grade = int(input("请输入你的成绩："))
#     if grade >= 90:
#         print("优秀")
#         pass
#     else:
#         print('你的成绩不达标')
#         print('建议去干饭')
#         pass
#     pass
# else:
#     print('建议回家')
#     pass


