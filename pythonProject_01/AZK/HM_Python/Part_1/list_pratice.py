"""
列表循环遍历操作
"""
# 练习案例：取出列表内的偶数
'''
定义一个列表，内容是：[1,2,3,4,5,6,7,8,9,10]
遍历列表取出列表中的偶数，并保存至一个新的列表对象中
使用while and for循环各操作一次
'''
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []
# for i in mylist:
#     if i % 2 == 0:
#         new_list.append(i)
print("原列表为:{}".format(mylist))
# print(f"该列表中的偶数组成的新列表为：{new_list}")

New_list = []
j = 0
while j < len(mylist):
    if mylist[j] % 2 == 0:
        New_list.append(mylist[j])
    j += 1
print("该列表中的偶数组成的新列表为：%s" % New_list)
