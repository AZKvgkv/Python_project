'''
序列练习
有字符串：“万过薪月, 员序程马黑来, nohtyP学”
请使用学过的任何方式，得到“黑马程序员”
'''

# 倒序字符串
Mystring = '万过薪月, 员序程马黑来, nohtyP学'

# 切片
print(Mystring[::-1])

# reverse 函数
Mystring_list = list(Mystring)
Mystring_list.reverse()
print(''.join(Mystring_list))

# 新建一个列表，从后往前添加元素
Mystring_list = []
for i in range(len(Mystring)-1, -1, -1):
    Mystring_list.append(Mystring[i])
print(''.join(Mystring_list))

'''法一'''
newstr = Mystring[::-1]
print(newstr[10:15])
str = Mystring[6:11]
print(str[::-1])
'''法二'''
newstr1 = Mystring.split(',')
newstr2 = newstr1[1].replace('来','')
newstr3 = newstr2.replace(' ','')[::-1]
print(newstr3)