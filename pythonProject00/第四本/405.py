#set是无序不支持索引和切片，且不重复的容器；类似于字典，但只有key，没有value
# set1={1,2,3}
# print(set1)
# dic1={1:3}
# print(dic1)


#添加操作
# set1={1,2,3}
# set1.add('xiaolaohu')
# print(set1)

#清空操作
# set1={1,2,3,4,5}
# set1.clear()
# print(set1)

#差集
# set2={2,3,4,5}
# o=set1.difference(set2)
# print(o)
# print(set1-set2)

#交集
# set1={1,2,3,4,5,6}
# set2={2,3,4,5,6,7,8}
# jcji=set1.intersection(set2)
# print(jcji)
# print(set1&set2)

#并集，使用上面的数据
# bji=set1.union(set2)
# print(bji)
# print(set1|set2)

#pop,从集合中拿数据并且同时删除
# print(set1)
# qudata=set1.pop()
# print(qudata)
# print(set1)

#discard 指定移除
# print(set1.discard(5))
# print(set1)

#update 两个集合的更新
# set1.update(set2)
# print(set1)