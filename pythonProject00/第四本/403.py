#序列范畴，str\tuple\list
# print(all([]))
#any 类似or，只要有一个为true,则结果就是true
# print(any((" ",False,0)))
# print(any((1,2,3,4,5,6)))
# print(any((0,0,0)))
#sort和sorted
# li=[2,45,8,7,90,10]
# # li.sort()#list排序方法，直接修改的是原始对象
# print('排序之前{}'.format(li))
# '''
# 升序排列
# '''
# afterli=sorted(li)
# print("升序排序之后{}".format(afterli))
# """
# 降序排列
# """
# afrevli=sorted(li,reverse=True)#降序排列
# print("降序排序之后{}".format(afrevli))
# tupleA=(2,34,5,23,67,9)
# va=sorted(tupleA,reverse=True)
# # va=sorted(tupleA)
# print(va)
#zip(),就是用来打包的,数量不一样时，按少的来压缩
# s1=['I','love','you']
# s2=['chen','xiao','qing']
# s3=["ni",'hao']
# print(list(zip(s1,s2,s3)))

def bookinfo():
    books=[]#存储所有的图书信息
    id = input("请输入编号：以空格间隔")
    bookname = input("请输入书名：以空格间隔")
    bookpos = input("请输入位置：以空格间隔")
    idlist = id.split(' ')
    namelist = id.split(' ')
    poslist = id.split(' ')
    bookinfo=zip(idlist,namelist,poslist)
    for bookitem in bookinfo:
        dictinfo={'编号':bookitem[0],'书名':bookitem[1],'位置':[2]}
        books.append(dictinfo)
        pass
    for item in books:
        print(item)
bookinfo()