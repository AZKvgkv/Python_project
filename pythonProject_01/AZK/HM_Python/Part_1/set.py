'''
集合，信息去重
有如下列表：
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
'''

myset = set()
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
for i in my_list:
    myset.add(i)
print(f"有列表{my_list}")
print("上述列表存入集合后的结果为%s" % myset)
print("上述列表存入集合后的结果为{}".format(myset))