'''
分割字符串
给定一个字符串：“itheima itcast boxuegu”
1.统计字符串内有多少个“it”字符
2.将字符串内的空格，全部替换成“|”
3.并按照“|”进行字符串分割
'''
mystring = "itheima itcast boxuegu"
print(f"字符串itheima itcast boxuegu内有{mystring.count('it')}个“it”字符")
newstring_1 = mystring.replace(' ', '|')
print("字符串itheima itcast boxuegu,将空格全部替换成“|”后的新字符串为:%s" % newstring_1)
newstring_2 = newstring_1.split('|')
print("字符串itheima|itcast|boxuegu按照“|”进行字符串分割后的新字符串为{}".format(newstring_2))
