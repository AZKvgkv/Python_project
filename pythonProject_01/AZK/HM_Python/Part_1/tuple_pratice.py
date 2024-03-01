'''
元组的基本操作
定义一个元组，内容是：('AZ',24,['football','music'])
通过元组的功能，对其
1.查询年龄所在下标
2.查询姓名
3.删除爱好中的football
4.增加爱好：coding到爱好list内
'''
mytuple = ('AZ', 24, ['football', 'music'])
print(f"年龄所在下标位置：{mytuple.index(24)}")
print("查询到的姓名为：%s" % mytuple[0])
mytuple[2].remove('football')
mytuple[2].append('coding')
print("经过增删之后的新元组为{}".format(mytuple))