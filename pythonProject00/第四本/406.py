#1.求三组连续自然数的和：1-10,20-30,35-45的三个和
# def sumrange(m,n):
#     '''
#     求m到n的连续自然数的总和
#     :param m:开始值 int
#     :param n:结束值 int
#     :return:
#     '''
#     return sum(range(m,n+1))
# print('1-10的和为%d'%sumrange(1,10))
# print('20-30的和为%d'%sumrange(20,30))
# print('35-45的和为%d'%sumrange(35,45))


#2.100个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三人吃1个馒头，问大小和尚各多少人？
# def personcount():
#     '''
#     计算各多少个和尚
#     大和尚dhs人，小和尚则100-dhs人
#     :return:
#     '''
#     for dhs in  range(1,100):
#         if 3*dhs+(100-dhs)*(1/3)==100:#100个和尚吃100个馒头
#             return (dhs,100-dhs)
#         pass
#     pass
# rsobj=personcount()
# print("大和尚{}人，小和尚{}人".format(rsobj[0],rsobj[1]))

#3.指定一个列表，列表里含有唯一一个只出现过一次的数字。写程序找出这个“独一无二”的数字
# li=[1,3,4,3,3,5,2,4,9,7,8,9,5,2,7]
# set1=set(li)
# # print(set1)
# for i in set1:
#     li.remove(i)
#     pass
# set2=set(li)#set2中为原来li中有重复的数字集合
# print(set2)


'''
print(set1-set2),这样也可以
print(set1.difference(set2))
'''


# for i in set1:#set1中数据全部去重后形成的集合
#     if i not in set2:
#         print(i)
#         pass
