#字符串操作
# test = 'python'
# print('指向第一个字符%s'%test[0])
# print('指向第二个字符%s'%test[1])
# print('将test首字母大写%s'%test.capitalize())
#去除两侧空格
# a="    hello,world    "
# print(id(a))#显示a的地址
# print(a.strip())
# print(a.rstrip()),右就是r,左就是l
# datastr='I am because you are'#,查找字符串
# # j="a"
# # # print(datastr.find(j))
# # print(datastr.index('e'))
# print(datastr.upper())#全部转换成大写
# print(datastr.lower())#全部转换成小写
# print(datastr[2:6])#切片操作，[start:end:step]左闭右开
# print(datastr[::-1])#倒叙输出


#列表操作
listA=[1,'郑奎','abcdef',True,3.14159265354]
# print(listA)#打印整个列表
# print(listA[2:4])
# print(listA[0])#输出第一个元素
# print(listA*2)#输出两倍
# listA.append('小老虎')#列表后增加元素
# listA.insert(2,'和小老虎')#插入到列表中某个特定的位置
# print(listA)

# redata=list(range(9))#强制转换为list对象
# print(redata)
# listA.extend(redata)#批量添加元素到列表里
# print(listA*2)

# listA[1]="小老虎"#修改
# del listA[3]#删掉某一项


# listA.pop(3)#移除指定元素所在项
# listA.remove("abcdef")#移除指定元素
# print(listA)

# o=listA.index('郑奎')#查找列表中某个元素的位置
# print(o)



#元组相关操作（不可变的序列）。主要用于查询，元组类型中，若只有一项，则在后面加个逗号
# a=(1,9.65,"小老虎",["aa",3,0.9,'ddd'])
# print(a)
# for i in a:
#     print(i,end=' ')
# print(a[1:3])
# print(a[:-2])#逆序每隔两个字符取一次
# a[3][0]='zhengkui'#可以对元组中的列表进行修改
# print(a)

# j=tuple(range(12))#与列表类似的操作
# print(type(j))
# q=(1,2,33,89,123,134,11,32,1)
# print(q.count(1))#用于统计该元组中所含元素的个数



#字典，用键来访问。无下标概念
# d={'n':"大老虎",'pro':"mine"}
# d['name']="小老虎"#格式：key:value
# # d['age']=22
# d['pos']="mine"
# # d.update({'age':21})#更新或增加某一项数据
# # del d["n"]#删除某一项数据
# # d.pop('pro')#同样可以删除某一项数据
# print(d)
# print(len(d))#获取字典的长度
# print(d['name'])#获取该字典中某个键的值
# print(d.keys())#打印所有的键
# print(d.values())#获取所有的值
# print(d.items())#获取所有的数据项
# for key,value in d.items():
#     print("%s==%s"%(key,value))
#     pass


#对字典进行排序，用key
# print(sorted(d.items(),key=lambda d:d[0]))
#对字典进行排序，用value
# print(sorted(d.items(),key=lambda d:d[1]))


#共有方法操作 + * in
# s1='人生苦短计算机太长'
# s2='计算机'
# print(s1+s2)
# print(s2 in s1)
# l1=[1,2,3]
# l2 =['a','b','c']
# print(l1+l2)
# print(s1*3)#几倍的复制
# dictionary={'name':'小老虎','time':'33'}
# print('time' in dictionary)#字典只用于键进行操作